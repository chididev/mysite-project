from .models import *
from django.views.generic import *
# Create your views here.


class CssView(ListView):
    model = Css
    template_name = 'cssacademy/css3.html'
    context_object_name = 'csss'


class CssDetail(DetailView):
    model = Css
    template_name = 'cssacademy/css_detail.html'
