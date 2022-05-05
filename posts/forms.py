from dataclasses import fields
from pyexpat import model
from django import forms


from .models import Post

MAX_POST_LENGTH = 240

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_POST_LENGTH:
            raise forms.ValidationError("This post is too long")
        return content