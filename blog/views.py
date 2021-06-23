from .models import Blog
from django.views.generic import *

# Create your views here.


# This lists all the items in the blog model
class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    ordering = ['-pk']


# This gives the detail view of the  blog object
class DetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'


# This handles the blog post creation process from the user
class CreateView(CreateView):
    model = Blog
    fields = '__all__'
    template_name = 'blog/create_blog.html'
