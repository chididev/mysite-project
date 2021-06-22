from .models import Html
from django.views.generic import *
# Create your views here.


class HtmlView(ListView):
    model = Html
    template_name = 'htmlacademy/html5.html'
    context_object_name = 'htmls'


class HtmlDetail(DetailView):
    model = Html
    template_name = 'htmlacademy/html_detail.html'
