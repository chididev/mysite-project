from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *


def codeacademy(request):
    return render(request, 'codeacademy/codeacademy.html')


@login_required
def html(request):
    htmls = Html.objects.all().order_by('-id')
    return render(request, 'codeacademy/html5.html', {'htmls': htmls})


def html_detail(request, html_id):
    html_detail = get_object_or_404(Html, pk=html_id)
    return render(request, 'codeacademy/html_detail.html', {'html': html_detail})


@login_required
def css(request):
    csss = Css.objects.all().order_by('-id')
    return render(request, 'codeacademy/css3.html', {'csss': csss})


def css_detail(request, css_id):
    css_detail = get_object_or_404(Css, pk=css_id)
    return render(request, 'codeacademy/css_detail.html', {'css': css_detail})


@login_required
def python(request):
    pythons = Python.objects.all().order_by('-id')
    return render(request, 'codeacademy/python.html', {'pythons': pythons})


def python_detail(request, python_id):
    python_detail = get_object_or_404(Python, pk=python_id)
    return render(request, 'codeacademy/python_detail.html', {'python': python_detail})


@login_required
def django(request):
    djangos = Django.objects.all().order_by('-id')
    return render(request, 'codeacademy/django.html', {'djangos': djangos})


def django_detail(request, django_id):
    django_detail = get_object_or_404(Django, pk=django_id)
    return render(request, 'codeacademy/python_detail.html', {'django': django_detail})
