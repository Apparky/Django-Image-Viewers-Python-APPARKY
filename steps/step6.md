## Step 6:

Now create `forms.py` file and edit it accordingly

```commandline
from django import forms
from .models import *


class PostInfo(forms.ModelForm):
    class Meta:
        model = Post_info
        fields = ['topic', 'description', 'images', 'img_alt']

```

This file make a connection between your `frontend` with your `backend`.

Your server is all set, It's time to set your `html` file to upload your images into your database.