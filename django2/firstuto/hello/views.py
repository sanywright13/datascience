from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello Wsanaa!!!")
def sanaa(request):
    return HttpResponse("Hello sanaa")
def greet(request,name):
        return HttpResponse(f"Hello, {name}")