from django.contrib import admin

from .models import Dishes, Category, Place

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title',  'category', 'place', 'price', 'is_public')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title_place',)}
    list_display = ('id', 'title_place')
    list_display_links = ('id', 'title_place')

