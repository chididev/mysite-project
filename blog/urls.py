from django.urls import path
from . import views
from django.views.generic import *
# from blog.views import blog

urlpatterns = [
    # url to the blog
    path('', views.BlogView.as_view(), name='blog'),
    # url to the blog object detail
    path('<pk>/detail/', views.DetailView.as_view(), name="detail"),
    # url to the create blog post
    path('create/', views.CreateView.as_view(), name='create'),
]
