from .models import *
from django.views.generic import *
# Create your views here.


# handles the portfolio/project listing in the portfolio page
class PortfolioView(ListView):
    model = Project
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'projects'
    ordering = ['-pk']
