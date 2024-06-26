# Generated by Django 4.2.11 on 2024-04-03 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Жанр')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('author', models.CharField(max_length=150, verbose_name='Автор')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('audio', models.FileField(blank=True, null=True, upload_to='audio/', verbose_name='Аудио')),
                ('video', models.FileField(blank=True, upload_to='video/', verbose_name='Видео')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата обновления')),
                ('is_published', models.BooleanField(default=True)),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='works.genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ['id'],
            },
        ),
    ]
