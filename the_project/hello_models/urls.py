from django.urls import path
from hello_models import views

# pylint: disable=invalid-name
app_name = 'models'

# pylint: disable=invalid-name
urlpatterns = [path('', views.index, name='index')]
