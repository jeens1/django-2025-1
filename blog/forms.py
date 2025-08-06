
from django import forms
from blog.models import Post
class PostForm(forms.ModelForm):
    class Meta:
            model=Post
            fields=['title',
                    'author',
                    'content',
                    'uploaded_image',
                    'category',
                    'uploaded_file']