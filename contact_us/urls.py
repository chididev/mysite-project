from django.urls import path
from . import views


urlpatterns = [
    # url to the contact us form
    path('', views.contact, name='contact'),

]
