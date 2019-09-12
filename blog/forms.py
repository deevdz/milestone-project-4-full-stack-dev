from django import forms
from tinymce import TinyMCE
from .models import Blog, Comment


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'slug', 'content', 'status', 'seo_title', 'seo_description',
        'tag', 'image', 'categories', 'featured', )


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': '',
        'id': 'usercomment',
        'rows': '4',
        'value': ''
        }), label='')
    class Meta:
        model = Comment
        fields = ('content', )