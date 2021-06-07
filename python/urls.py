from django.urls import path
from . import views
from python.views import *

urlpatterns = [
    path('python/', views.python, name='python'),
    path('<int:python_id>/', views.python_detail, name="python_detail"),
]
