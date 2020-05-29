from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailMixin

# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

# def post_details(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_details.html', context={'post': post})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_details.html'

    #def get(self, request, slug):
    #    # post = Post.objects.get(slug__iexact=slug)         #реалізуємо те саме за допомогою get_object_or_404
    #    post = get_object_or_404(Post, slug__iexact=slug)    #Додаємо вивід 404, якщо сторінки не існує. get_object_or_404(try catch)
    #    return render(request, 'blog/post_details.html', context={'post': post})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag})

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

    # def get(self, request, slug):
    #     # tag = Tag.objects.get(slug__iexact=slug)
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'blog/tag_detail.html', context={'tag': tag})






