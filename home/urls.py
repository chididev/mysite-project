from django.urls import path
from . import views
from django.views.generic import *


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
