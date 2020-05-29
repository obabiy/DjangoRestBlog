from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list_url'),  #Задаємо ім'я посиланню і потім звертаємося по ньому (Щоб при зміні url не довелося міняти всі path)
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail_url')
]