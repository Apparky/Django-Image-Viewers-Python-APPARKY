## Step 2:

Now open the project file with the `IDLE` you like to use

Open the `terminal` from your `IDLE` and type 

```commandline
python manage.py runserver
```

> And you are good to go. Open this link form you browser [http://localhost:8000/](http://localhost:8000/)
> 
> You will see the `server` is running
> 
> 

Now Let's Create an application for it to `Upload` and `View` Images.

For Creating an Application type this to your `terminal`

```commandline
python manage.py startapplications imageviewer
```

You can see now a new folder has been created to your project directory

Now go to `settings.py` file you will find some list of installed application there

```commandline
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
]
```

add the application name and save the file

```commandline
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'imageviewer', # app name has to insert here to make it work
]
```

like this


After that go to the application folder and create a new file named `urls.py`. Now you just have to register the application url to the project url like this

```commandline
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imageviewer.urls'))
]

```

Go back to project application directory, and open `urls.py`, edit the file accordingly

```commandline
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/', views.viewer, name='viewer')
]

```

Now come back to Application directory and open `views.py` file

You can copy and paste the `code` from here

```commandline
from django.shortcuts import render
from .models import *
from imageviewer.forms import PostInfo


def index(request):
    if request.method == 'POST':
        post = Post_info()

        topic = request.POST.get('topic')
        description = request.POST.get('description')
        images = request.FILES['image']

        post.topic = topic
        post.description = description
        post.images = images
        post.img_alt = 'Default ALT TAG'

        form = PostInfo(request.POST, request.FILES)
        if form.is_valid():
            post.save()

            return render(request, 'success.html')

    return render(request, 'index.html')


def viewer(request):
    posts = Post_info.objects.all()
    return render(request, 'view.html', {'posts': posts})



```

Now the `server` is ready to go.