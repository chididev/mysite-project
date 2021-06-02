from django.urls import path
from . import views
from blog.views import blog

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('<int:blog_id>/', views.detail, name="detail"),
]
