from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *


def codeacademy(request):
    return render(request, 'codeacademy/codeacademy.html')


def html(request):
    htmls = Html.objects.all().order_by('-id')
    return render(request, 'codeacademy/html5.html', {'htmls': htmls})


def html_detail(request, html_id):
    html_detail = get_object_or_404(Html, pk=html_id)
    return render(request, 'codeacademy/html_detail.html', {'html': html_detail})
