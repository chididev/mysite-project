from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    # url to the django list object page
    path('django/', views.DjangoView.as_view(), name='django'),
    # url to the django detail page
    path('<pk>/django_detail', views.DjangoDetail.as_view(), name='django_detail'),
]
