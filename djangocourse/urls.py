from django.urls import path
from . import views
from codeacademy.views import *

urlpatterns = [
    path('django/', views.django, name='django'),
    path('<int:django_id>/', views.django_detail, name='django_detail'),
]
