from django.urls import path
from . import views
from codeacademy.views import *

urlpatterns = [
    path('', views.codeacademy, name='codeacademy'),
    path('html/', views.html, name='html'),
    path('css/', views.css, name='css'),
    path('python/', views.python, name='python'),
    path('django/', views.django, name='django'),
]
