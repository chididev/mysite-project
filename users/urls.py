from django.urls import path
from . import views as auth_views
from django.contrib.auth import views

urlpatterns = [
    # url to user registeration page
    path('register/', auth_views.register, name='register'),
    # url to user login page
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # url to user logout page
    path('logout/', views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
