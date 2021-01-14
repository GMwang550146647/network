from django.shortcuts import render
from books.models import MultiTableManagement
from django.shortcuts import render, HttpResponse, redirect, reverse
# Create your views here.

def database(request):
    MultiTableManagement().run()
    return HttpResponse('Database Management: Multi Table Management')
