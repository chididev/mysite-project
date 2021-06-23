from django.views.generic import *

# Create your views here.


# handles the home page
class HomeView(TemplateView):
    template_name = 'home/home.html'
