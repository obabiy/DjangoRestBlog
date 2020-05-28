from django.db import models


# Create your models here.

# Додаємо клас(таблицю) в базу данних
class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):                               #вказуєм форматування данних які будуть виводитись
        return '{}'.format(self.title)
