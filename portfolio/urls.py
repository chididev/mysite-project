from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    # url to the portfolio page
    path('', views.PortfolioView.as_view(), name='portfolio'),
]
