from django.db import models
from django.shortcuts import reverse

# Create your models here.

# Додаємо клас(таблицю) в базу данних
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)   #те, що буде заміняти айдішку в url і буде зрозуміле людині
    body = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')    #blank дає можливість не додавати теги до постів; related_name - з'являється в класі Тег, після додавання будь-якого тегу будь-якому посту
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})   #додаємо метод, який визначає url з відповідим slug для кожного посту

    def __str__(self):                               #вказуєм форматування данних які будуть виводитись
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title