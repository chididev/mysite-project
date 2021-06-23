from .models import *
from django.views.generic import *
# Create your views here.


# lists the css objects in the css model
class CssView(ListView):
    model = Css
    template_name = 'cssacademy/css3.html'
    context_object_name = 'csss'


# handles the detail css objects
class CssDetail(DetailView):
    model = Css
    template_name = 'cssacademy/css_detail.html'
