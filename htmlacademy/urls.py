from django.views.generic import *
from . import views
from django.urls import path

urlpatterns = [
    # url to the html academy page
    path('html/', views.HtmlView.as_view(), name='html'),
    # url to the html detail page
    path('<pk>/htmldetail', views.HtmlDetail.as_view(), name='html_detail'),
]
