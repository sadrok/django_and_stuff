from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView, DetailView, CreateView, UpdateView, DeleteView)

from .forms import PostForm
from .models import Post


class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostListView(ListView):
    template_name = 'blog/posts.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()) \
            .order_by('-published_date')


class PostDetailView(DetailView):
    template_name = 'blog/post.html'
    model = Post


class PostCreateView(CreateView, LoginRequiredMixin):
    template_name = 'blog/create.html'
    model = Post
    form_class = PostForm

    login_url = '/login'
    redirect_field_name = 'blog/post.html'


class PostUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'blog/edit.html'
    model = Post
    form_class = PostForm

    login_url = '/login'
    redirect_field_name = 'blog/post.html'


class PostDeleteView(DeleteView, LoginRequiredMixin):
    template_name = 'blog/delete.html'
    model = Post
    success_url = reverse_lazy('blog')

    login_url = '/login'
    redirect_field_name = 'blog/posts.html'


class DraftListView(ListView, LoginRequiredMixin):
    template_name = 'blog/posts.html'
    model = Post

    login_url = '/login'
    redirect_field_name = 'blog/posts.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True) \
            .order_by('created_date')
