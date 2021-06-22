from .models import *
from django.views.generic import *
# Create your views here.


class PortfolioView(ListView):
    model = Project
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'projects'
    ordering = ['-pk']
