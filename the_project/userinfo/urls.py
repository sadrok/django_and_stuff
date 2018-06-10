from django.urls import path, re_path
from userinfo import views

# pylint: disable=invalid-name
app_name = 'userinfo'

# pylint: disable=invalid-name
urlpatterns = [
    path('', views.UserListView.as_view(), name='index'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    re_path(r'^(?P<pk>[0-9]+)$', views.UserInfoView.as_view(), name='info'),
    re_path(r'^(?P<pk>[0-9]+)/edit$', views.edit, name='edit'),
]
