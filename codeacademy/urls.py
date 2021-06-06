from django.urls import path
from . import views
from codeacademy.views import *

urlpatterns = [
    path('', views.codeacademy, name='codeacademy'),
    path('html/', views.html, name='html'),
    path('css/', views.css, name='css'),
    path('python/', views.python, name='python'),
    path('django/', views.django, name='django'),
    path('<int:html_id>', views.html_detail, name="html_detail"),
    path('<int:css_id>', views.css_detail, name="css_detail"),
    path('<int:python_id>', views.python_detail, name="python_detail"),
    path('<int:django_id>', views.django_detail, name="django_detail"),
]
