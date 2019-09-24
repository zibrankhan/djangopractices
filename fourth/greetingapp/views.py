from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greeting_view(request):
    return HttpResponse('<h1> Hello Friends Good Morning And Have a Nice Day:: </h1>')