from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def codeacademy(request):
    return render(request, 'codeacademy/codeacademy.html')


@login_required
def html(request):
    return render(request, 'codeacademy/html5.html')


@login_required
def css(request):
    return render(request, 'codeacademy/css3.html')


@login_required
def python(request):
    return render(request, 'codeacademy/python.html')


@login_required
def django(request):
    return render(request, 'codeacademy/django.html')
