from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import *

class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        # post = Post.objects.get(slug__iexact=slug)         #реалізуємо те саме за допомогою get_object_or_404
        obj = get_object_or_404(self.model, slug__iexact=slug)    #Додаємо вивід 404, якщо сторінки не існує. get_object_or_404(try catch)
        return render(request, self.template, context={self.model.__name__.lower(): obj})