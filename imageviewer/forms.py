from django import forms
from .models import *


class PostInfo(forms.ModelForm):
    class Meta:
        model = Post_info
        fields = ['topic', 'description', 'images', 'img_alt']


