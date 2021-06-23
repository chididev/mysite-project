from django.views.generic import *


# The logic behind  the codeacademy page
class AcademyView(TemplateView):
    template_name = 'codeacademy/codeacademy.html'
