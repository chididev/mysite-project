from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path('', views.PortfolioView.as_view(), name='portfolio'),
]
