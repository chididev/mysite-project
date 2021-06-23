from django.urls import path
from . import views
from django.views.generic import *


urlpatterns = [
    # url to the home page
    path('', views.HomeView.as_view(), name='home'),
]
