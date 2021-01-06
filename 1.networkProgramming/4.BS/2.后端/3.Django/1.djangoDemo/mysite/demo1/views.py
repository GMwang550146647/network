from django.shortcuts import render
from django.shortcuts import render, HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Demo1 Home")

def index(request):
    return HttpResponse("Demo1 Index")