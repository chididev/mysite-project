from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path('django/', views.DjangoView.as_view(), name='django'),
    path('<pk>/django_detail', views.DjangoDetail.as_view(), name='django_detail'),
]
