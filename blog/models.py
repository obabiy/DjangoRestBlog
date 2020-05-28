from django.db import models
from django.shortcuts import reverse

# Create your models here.

# Додаємо клас(таблицю) в базу данних
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)   #те, що буде заміняти айдішку в url і буде зрозуміле людині
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})   #додаємо метод, який визначає url з відповідим slug для кожного посту

    def __str__(self):                               #вказуєм форматування данних які будуть виводитись
        return '{}'.format(self.title)
