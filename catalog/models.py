from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=255,
        verbose_name='Категория',
    )

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


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
        upload_to='catalog/images/',
        verbose_name='Изображение',
    )
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title


class Review(models.Model):

    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.PROTECT,
        verbose_name='Товар'
    )

    name = models.CharField(
        max_length=255,
        verbose_name='Имя',
    )

    rating = models.IntegerField(verbose_name='Рейтинг')
    review = models.TextField(verbose_name='Отзыв')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name
