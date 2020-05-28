from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def post_details(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_details.html', context={'post': post})