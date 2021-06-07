from django.urls import path
from . import views
from codeacademy.views import htmldetail

urlpatterns = [
    path('', views.codeacademy, name='codeacademy'),
    path('html/', views.html, name='html'),
    path('<int:html_id>/', views.htmldetail, name="html_detail"),
]
