## Step 5:

On the `application` Directory open `models.py` and edit it accordingly

```commandline
from django.db import models


# Create your models here.
class Post_info(models.Model):
    topic = models.CharField(max_length=300)
    description = models.TextField()
    images = models.FileField(upload_to='midea/images', blank=True)
    img_alt = models.CharField(max_length=100, null=True, blank=True, default='image_alt')

    def __str__(self):
        return self.topic


```

After that open `admin.py` and edit it accordingly

```commandline
from django.contrib import admin
from .models import *

admin.site.register(Post_info)

```

By this your `database` is ready to store all `Images` Information.

[__Django__](https://www.djangoproject.com/) use [sqlite3](https://sqlite.org/index.html) as a default `database`. To know more about [sqlite3](https://sqlite.org/index.html) Click [Here](https://sqlite.org/index.html)
