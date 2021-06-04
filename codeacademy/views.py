from django.shortcuts import render


# Create your views here.
def codeacademy(request):
    return render(request, 'codeacademy/codeacademy.html')
