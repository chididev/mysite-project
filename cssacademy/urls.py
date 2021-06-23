from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    # url to the css object list
    path('css/', views.CssView.as_view(), name='css'),
    # url to the css detail page
    path('<pk>/css_detail/', views.CssDetail.as_view(), name="css_detail"),
]
