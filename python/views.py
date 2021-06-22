from .models import *
from django.views.generic import *
# Create your views here.


class PythonView(ListView):
    model = Python
    template_name = 'python/python.html'
    context_object_name = 'pythons'


class PythonDetail(DetailView):
    model = Python
    template_name = 'python/python_detail.html'
