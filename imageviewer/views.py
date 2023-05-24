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
