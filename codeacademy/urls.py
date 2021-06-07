from django.urls import path
from . import views
from codeacademy.views import html_detail

urlpatterns = [
    path('', views.codeacademy, name='codeacademy'),
    path('html/', views.html, name='html'),
    path('<int:html_id>/', views.html_detail, name="html_detail"),
]
