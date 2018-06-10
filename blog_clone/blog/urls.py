from django.urls import path, re_path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    path('drafts', views.DraftListView.as_view(), name='drafts'),
    path('about', views.AboutView.as_view(), name='about'),
    path('post/new/', views.PostCreateView.as_view(), name='new'),
    re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post'),
    re_path(r'^post/(?P<pk>\d+)/edit$',views.PostUpdateView.as_view(), name='edit'),
    re_path(r'^post/(?P<pk>\d+)/delete',views.PostDeleteView.as_view(), name='delete'),
]
