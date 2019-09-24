from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_world_view(request):
    return HttpResponse('<h1>Hello this is the response from the Django Application My Name Is Khan </h1>')

