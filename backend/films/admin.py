from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id',  'title_ru', 'title_orig',  'prod_year', 'timing', 'premiere_date', 'country', 'genre', 'director', 'poster')

 
