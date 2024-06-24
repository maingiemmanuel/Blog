from django import forms
from BApp.models import Blogs


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'
