from django.urls import path
from . import views
# from recipes.views import home

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipes, name="recipe"),
    path('recipes/category/<int:category_id>/', views.category, name="category")
]

