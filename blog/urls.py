from django.urls import path
from . import views
from blog.views import blog

urlpatterns = [
    path('blog/', views.blog, name='blog'),
]
