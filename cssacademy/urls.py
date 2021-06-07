from django.urls import path
from . import views
from cssacademy.views import *

urlpatterns = [
    path('css/', views.css, name='css'),
    path('<int:css_id>/', views.css_detail, name="css_detail"),
]
