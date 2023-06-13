from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'wendellast'
            }
)
    
def recipes(request, id):
    return render(request, 'recipes/pages/recipe-views.html', context={
        'name': 'wendellast'
            }
)
    