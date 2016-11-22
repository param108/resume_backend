"""resume_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import views
from resume_backend import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^project/(?P<pid>[0-9]+)/$', views.update_project),
    url(r'^project/$', views.manage_project),
    url(r'^view/$', views.show_resume),
    url(r'^data/(?P<year>[0-9]+)/$', views.data)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
