from django.db import models
from django.urls import reverse


class Catalog(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Каталог',
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'catalog:catalog',
            kwargs={'catalog_slug': self.slug}
        )


class Category(models.Model):
    catalog = models.ForeignKey(
        Catalog,
        on_delete=models.PROTECT,
        related_name='categories',
        verbose_name='Каталог',
    )

    name = models.CharField(
        max_length=255,
        verbose_name='Категория',
    )

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-id',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'catalog:product_list_by_category',
            kwargs={'category_slug': self.slug}
        )


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='products',
        verbose_name='Категория',
    )

    title = models.CharField(
        max_length=255,
        verbose_name='Наименование',
    )

    description = models.TextField(verbose_name='Описание')

    image = models.ImageField(
        upload_to='catalog/',
        verbose_name='Изображение',
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'catalog:product_detail',
            kwargs={
                'product_slug': self.slug,
                'category_slug': self.category.slug
            }
        )


class Review(models.Model):

    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.PROTECT,
        verbose_name='Товар'
    )

    name = models.CharField(
        max_length=64,
        verbose_name='Имя',
    )

    rating = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг'
    )
    review = models.TextField(
        max_length=255,
        verbose_name='Отзыв'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name
