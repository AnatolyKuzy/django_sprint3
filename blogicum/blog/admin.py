from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Post, Category, Location

# Отменяем регистрацию модели Group в админке
admin.site.unregister(Group)

admin.site.register(Category)
admin.site.register(Location)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('text', )
    list_display = (
        'id', 'title', 'author', 'is_published',
        'text', 'category', 'pub_date',
        'location', 'created_at',
    )
    list_display_links = ('title',)
    list_editable = ('category', 'is_published', 'location',)
    list_filter = ('created_at', )
    empty_value_display = '-пусто-'
