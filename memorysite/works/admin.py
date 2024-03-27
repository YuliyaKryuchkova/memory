from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class WorksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'time_create',
        'get_html_photo',
        'is_published'
    )
    list_display_links = (
        'id',
        'title'
    )
    search_fields = (
        'title',
        'description'
    )
    list_editable = (
        'is_published',
    )
    list_filter = (
        'is_published',
        'time_create'
    )
    prepopulated_fields = {
        'slug': ('title',)
    }
    fields = (
        'title',
        'slug',
        'genre',
        'author',
        'description',
        'photo',
        'audio',
        'video',
        'get_html_photo',
        'is_published',
        'time_create',
        'time_update'
    )
    readonly_fields = (
        'time_create',
        'time_update',
        'get_html_photo'
    )
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Миниатюра'


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    list_display_links = (
        'id',
        'name'
    )
    search_fields = (
        'name',
    )
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Works, WorksAdmin)
admin.site.register(Genre, GenreAdmin)
