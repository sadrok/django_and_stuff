from django.urls import path, re_path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    path('drafts', views.DraftListView.as_view(), name='drafts'),
    path('about', views.AboutView.as_view(), name='about'),
    path('post/new/', views.PostCreateView.as_view(), name='new'),
    re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post'),
    re_path(r'^post/(?P<pk>\d+)/edit$', views.PostUpdateView.as_view(), name='edit'),
    re_path(r'^post/(?P<pk>\d+)/delete', views.PostDeleteView.as_view(), name='delete'),
    re_path(r'^post/(?P<pk>\d+)/comment', views.add_comment_to_post, name='comment'),
    re_path(r'^post/(?P<pk>\d+)/publish', views.publish_post, name='publish'),
    re_path(r'^comment/(?P<pk>\d+)/approve', views.approve_comment, name='approve_comment'),
    re_path(r'^comment/(?P<pk>\d+)/remove', views.remove_comment, name='remove_comment'),
]
