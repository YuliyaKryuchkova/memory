from django.db import models


class Works(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='URL'
    )
    author = models.CharField(
        max_length=150,
        verbose_name='Автор'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    audio = models.FileField(
        upload_to='audio/',
        verbose_name='Аудио',
        blank=True,
        null=True
    )
    video = models.FileField(
        upload_to='video/',
        blank=True,
        verbose_name='Видео'
    )
    photo = models.ImageField(
        upload_to='photos/',
        verbose_name='Фото',
        blank=True,
        null=True
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Дата создания'
    )
    time_update = models.DateTimeField(
        auto_now=True,
        db_index=True,
        verbose_name='Дата обновления'
    )
    is_published = models.BooleanField(
        default=True
    )
    genre = models.ForeignKey(
        'Genre',
        verbose_name='Жанр',
        on_delete=models.PROTECT,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ['id']


class Genre(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Жанр'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['id']
