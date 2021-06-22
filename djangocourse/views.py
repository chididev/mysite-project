from .models import *
from django.views.generic import *
# Create your views here.


class DjangoView(ListView):
    model = Django
    template_name = 'djangocourse/django.html'
    context_object_name = 'djangos'


class DjangoDetail(DetailView):
    model = Django
    template_name = 'djangocourse/django_detail.html'
