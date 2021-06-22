from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path('css/', views.CssView.as_view(), name='css'),
    path('<pk>/css_detail/', views.CssDetail.as_view(), name="css_detail"),
]
