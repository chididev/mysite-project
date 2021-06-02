from django.shortcuts import render
from .models import *
# Create your views here.
def portfolio(request):
    projects = Project.objects.all().order_by('-id')
    return render(request, 'portfolio/portfolio.html', {'projects':projects})
