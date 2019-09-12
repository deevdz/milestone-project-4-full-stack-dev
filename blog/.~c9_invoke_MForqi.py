from django import forms
from tinymce import TinyMCE
from .models import Blog, Comment


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class BlogForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Blog
        fields = ('title', 'slug' 'content', 'status', 'seo_title', 'seo_description',
        'tag', 'image', 'categories', 'featured', )


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        fields = ('content', )