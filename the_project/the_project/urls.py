"""the_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path
from django.views.static import serve

from hello_world.views import index as home_index


urlpatterns = [
    path('', home_index, name='home'),
    path('hello/', include('hello_world.urls'), name='hello'),
    path('models/', include('hello_models.urls'), name='models'),
    path('forms/', include('hello_forms.urls'), name='forms'),
    path('users/', include('userinfo.urls'), name='userinfo'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns.append(
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        })
    )
