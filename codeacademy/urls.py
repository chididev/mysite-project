from django.urls import path
from . import views
from codeacademy.views import codeacademy

urlpatterns = [
    path('', views.codeacademy, name='codeacademy'),
]
