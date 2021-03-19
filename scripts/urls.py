from django.urls import path

from . import views

app_name = 'scripts'
urlpatterns = [
	path('', views.index, name='index'),
]