"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url to the admin site
    path('admin/', admin.site.urls),
    # url to the home app
    path('', include('home.urls')),
    # url to the portfolio app
    path('portfolio/', include('portfolio.urls')),
    # url to the blog app
    path('blog/', include('blog.urls')),
    # url to the codeacademy app
    path('codeacademy/', include('codeacademy.urls')),
    # url to the contact us app
    path('contact/', include('contact_us.urls')),
    # url to the html academy app
    path('html5/', include('htmlacademy.urls')),
    # url to the css academy app
    path('css3/', include('cssacademy.urls')),
    # url to the python  app
    path('python/', include('python.urls')),
    # url to the django app
    path('django/', include('djangocourse.urls')),
    # url to the users app
    path('accounts/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # url to the media file storage
