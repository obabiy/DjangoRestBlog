from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def posts_list(request):
    n = ["Alex","Oleg","Maks","Olia"]
    return render(request, 'blog/index.html', context={'names': n})
