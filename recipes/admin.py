from django.contrib import admin
from . models import Category, Recipe

# Register your models here.
class CateogoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...
    

admin.site.register(Category, CateogoryAdmin)