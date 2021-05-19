from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('sport2', views.as2, name="sport2"),
	path('initialize', views.make_data, name="make_data"),
]
