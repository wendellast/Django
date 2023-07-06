from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe


def home(request):
    recipe = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipe,
    })
    
def category(request, category_id):
    recipe = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipe,
    })
    
def recipes(request, id):
    return render(request, 'recipes/pages/recipe-views.html', context={
        'recipe': make_recipe(),
        'is_datail_page': True
            }
)
    