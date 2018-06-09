
from django.urls import path
from hello_forms import views

# pylint: disable=invalid-name
urlpatterns = [
    path('', views.index, name='index')
]
