from django.views.generic import *
from . import views
from django.urls import path

urlpatterns = [
    path('html/', views.HtmlView.as_view(), name='html'),
    path('<pk>/htmldetail', views.HtmlDetail.as_view(), name='html_detail'),
]
