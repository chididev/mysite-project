from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    # url to the codeacademy page
    path('', views.AcademyView.as_view(), name='codeacademy'),
]
