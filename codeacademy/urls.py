from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path('', views.AcademyView.as_view(), name='codeacademy'),
]
