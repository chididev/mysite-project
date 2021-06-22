from django.views.generic import *

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home/home.html'
