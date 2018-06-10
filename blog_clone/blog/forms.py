from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text']

        # HTML STUFF for CSS STYLING!
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'textinputclass'
            }),
            'text': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea postcontent'
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'author_email', 'text']

        # HTML STUFF for CSS STYLING!
        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'textinputclass'
            }),
            'author_email': forms.EmailInput(attrs={
                'class': 'textinputclass'
            }),
            'text': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea',
                'rows': 1
            })
        }
