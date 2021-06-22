from django.urls import path
from . import views
from django.views.generic import *
# from blog.views import blog

urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('<pk>/detail/', views.DetailView.as_view(), name="detail"),
    path('create/', views.CreateView.as_view(), name='create'),
]
