from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (
    TemplateView,
    ListView, DetailView, CreateView, UpdateView, DeleteView)

from .forms import PostForm, CommentForm
from .models import Post, Comment


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
    template_name = 'blog/drafts.html'
    model = Post

    login_url = '/login'
    redirect_field_name = 'blog/posts.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True) \
            .order_by('created_date')


###############################################################################
###############################################################################

@login_required
def publish_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post', pk=post.pk)


# @login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment.html', {'form': form})


@login_required
def approve_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post', pk=comment.post.pk)


@login_required
def remove_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post', pk=post_pk)
