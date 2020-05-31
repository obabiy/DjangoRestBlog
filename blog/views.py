from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm


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

class PostCreate(ObjectCreateMixin, View):

    model_form = PostForm
    template = 'blog/post_create_form.html'

    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create_form.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #     if bound_form.is_valid():                                                                        #Робимо шаблон (Mixin) для однакових форм додавання постів і тегів
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create_form.html', context={'form': bound_form})


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'

class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts _list_url'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

    # def get(self, request, slug):
    #     # tag = Tag.objects.get(slug__iexact=slug)
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'blog/tag_detail.html', context={'tag': tag})

class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'


    # def get(self, request):
    #     form = TagForm()
    #     return render(request, 'blog/tag_create.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = TagForm(request.POST)                                                      #Робимо шаблон (Mixin) для однакових форм додавання постів і тегів
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_create.html', context=({'form': bound_form}))

class TagUpdate(ObjectUpdateMixin, View):

    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'


    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag':tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)                                                     #Робимо шаблон (Mixin) для однакових форм редагування постів і тегів
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_update_form.html', context={'form': bound_form, 'tag':tag})

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'

    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact = slug)
    #     return render(request, 'blog/tag_delete_form.html', context={'tag': tag})
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact = slug)
    #     tag.delete()
    #     return redirect(reverse('tags_list_url'))




def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag})


