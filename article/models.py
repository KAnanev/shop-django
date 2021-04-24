from django.db import models

from catalog.models import Product


class Article(models.Model):
    name = models.CharField(max_length=128, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Основной текст')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    products = models.ManyToManyField(Product, verbose_name='Товары', blank=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name
