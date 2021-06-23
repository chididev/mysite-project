from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    # url to the python academy page
    path('python/', views.PythonView.as_view(), name='python'),
    # url to python academy detail page
    path('<pk>/python_detail/', views.PythonDetail.as_view(), name="python_detail"),
]
