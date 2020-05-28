from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url')   #Задаємо ім'я посиланню і потім звертаємося по ньому (Щоб при зміні url не довелося міняти всі path)
]