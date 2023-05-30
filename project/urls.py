from django.contrib import admin
from django.http import HttpResponse
from django.urls import path


def myView(request):
    return HttpResponse('Hello World')


def home(request):
    return HttpResponse('Home')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sobre/', myView),
    path('', home)
]
