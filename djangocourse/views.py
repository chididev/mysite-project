from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *


def django(request):
    djangos = Django.objects.all().order_by('-id')
    return render(request, 'djangocourse/django.html', {'djangos': djangos})


def django_detail(request, django_id):
    django_detail = get_object_or_404(Django, pk=django_id)
    return render(request, 'djangocourse/django_detail.html', {'django': django_detail})
