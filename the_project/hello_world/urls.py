from django.urls import path
from hello_world import views

# pylint: disable=invalid-name
app_name = 'hello'

# pylint: disable=invalid-name
urlpatterns = [path('', views.IndexView.as_view(), name='index')]
