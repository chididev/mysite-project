from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


@login_required
def css(request):
    csss = Css.objects.all().order_by('-id')
    return render(request, 'cssacademy/css3.html', {'csss': csss})


def css_detail(request, css_id):
    css_detail = get_object_or_404(Css, pk=css_id)
    return render(request, 'cssacademy/css_detail.html', {'css': css_detail})
