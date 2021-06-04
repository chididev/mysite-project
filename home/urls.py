from django.urls import path
from . import views
from home.views import home


urlpatterns = [
    path('', views.home, name='home'),
]
