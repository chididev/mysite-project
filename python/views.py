from .models import *
from django.views.generic import *
# Create your views here.


# handles the python object listing in the python page
class PythonView(ListView):
    model = Python
    template_name = 'python/python.html'
    context_object_name = 'pythons'


# handles the python object detailing
class PythonDetail(DetailView):
    model = Python
    template_name = 'python/python_detail.html'
