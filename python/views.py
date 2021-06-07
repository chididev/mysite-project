from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


@login_required
def python(request):
    pythons = Python.objects.all().order_by('-id')
    return render(request, 'python/python.html', {'pythons': pythons})


def python_detail(request, python_id):
    python_detail = get_object_or_404(Python, pk=python_id)
    return render(request, 'python/python_detail.html', {'python': python_detail})
