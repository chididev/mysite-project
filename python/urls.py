from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path('python/', views.PythonView.as_view(), name='python'),
    path('<pk>/python_detail/', views.PythonDetail.as_view(), name="python_detail"),
]
