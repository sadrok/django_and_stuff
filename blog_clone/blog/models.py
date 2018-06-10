from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now
        self.save()

    @property
    def approved_comments(self):
        return self.comments.filter(approved=True)

    def get_absolute_url(self):
        '''
        :return: The url of this Post
        '''
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    # author may be anonymous
    author = models.CharField(max_length=200, blank=True, null=True)
    # and emails are required but not shown on site
    author_email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        '''
        TODO: Creating a comment will be an AJAX function soon
        :return: The url of the post commented on
        '''
        return reverse('post_detail', kwargs={'pk': self.post.pk})

    def __str__(self):
        return self.text
