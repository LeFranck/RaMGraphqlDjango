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
	retorno = await RaMClient.run_second_round(RaMClient)
	data = {
		"round_2": retorno,
	}
	return JsonResponse(data)