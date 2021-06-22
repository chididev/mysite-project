from .models import Blog
from django.views.generic import *
# Create your views here.


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    ordering = ['-pk']


class DetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'


class CreateView(CreateView):
    model = Blog
    fields = '__all__'
    template_name = 'blog/create_blog.html'
