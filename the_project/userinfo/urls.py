from django.urls import path, re_path
from userinfo import views

# pylint: disable=invalid-name
app_name = 'userinfo'

# pylint: disable=invalid-name
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    re_path(r'^(?P<user_id>[0-9]+)$', views.info, name='info'),
    re_path(r'^(?P<user_id>[0-9]+)/edit$', views.edit, name='edit'),
]
