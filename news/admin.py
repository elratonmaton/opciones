from django.contrib import admin

from news.models import Category, Autor, News


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display


class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'names', 'last_names')
    list_display_links = list_display


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'autor')
    list_display_links = list_display


admin.site.register(Category, CategoryAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(News, NewsAdmin)
