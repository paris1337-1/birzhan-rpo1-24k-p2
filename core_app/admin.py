from django.contrib import admin
from .models import Category, City, Ad, Favorite


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'city', 'price', 'is_moderated', 'is_top', 'created_at')
    list_filter = ('is_moderated', 'is_top', 'category', 'city')
    list_editable = ('is_moderated', 'is_top')
    search_fields = ('title', 'author__username')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'ad')
