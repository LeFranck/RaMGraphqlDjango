from django.urls import path

from . import views

app_name = 'scripts'
urlpatterns = [
	path('', views.index, name='index'),
	path('round_1/', views.round_1, name='round_1'),
	path('round_2/', views.round_2, name='round_2'),
	path('round_2/api/', views.round_2_api, name='round_2_api'),
	path('char_query_api/', views.char_query_api, name='char_query_api'),
]