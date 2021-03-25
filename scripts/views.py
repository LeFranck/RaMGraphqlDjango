from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.http import Http404
from django.http import JsonResponse
from scripts.models import RaMClient
from scripts.models import RaMQuerys
from asgiref.sync import sync_to_async
from asgiref.sync import async_to_sync
import asyncio
from python_graphql_client import GraphqlClient



# Create your views here.
def index(request):
	context = {}
	return render(request, 'scripts/index.html', context)

async def round_1(request):
	retorno = await RaMClient.run_first_round(RaMClient)
	data = {
		"round_1": retorno
	}
	return JsonResponse(data)

async def round_2(request):
	retorno = await RaMClient.run_second_round(RaMClient, True)
	data = {
		"round_2": retorno,
	}
	return JsonResponse(data)

async def round_2_api(request):
	retorno = await RaMClient.run_second_round(RaMClient, False)
	data = {
		"round_2": retorno,
	}
	return JsonResponse(data)

async def char_query_api(request):
	schema = request.GET.get("schema")
	char = request.GET.get("char")
	if not schema:
		raise Http404("Did not get a char")	
	if not char:
		raise Http404("Did not get a char")	
	if char == "":
		raise Http404("Did not get a char")	
	if schema == "locations" or schema == "characters" or schema == "episodes":
		retorno = await RaMClient.char_query_api(RaMClient, schema, char[0])
		data = {
			"char_query": retorno
		}
		return JsonResponse(data)
	else:
		raise Http404("Did not get a corret schema")
