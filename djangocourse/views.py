from .models import *
from django.views.generic import *
# Create your views here.


# Lists the objects in the django model
class DjangoView(ListView):
    model = Django
    template_name = 'djangocourse/django.html'
    context_object_name = 'djangos'


# Handles the django object details
class DjangoDetail(DetailView):
    model = Django
    template_name = 'djangocourse/django_detail.html'
