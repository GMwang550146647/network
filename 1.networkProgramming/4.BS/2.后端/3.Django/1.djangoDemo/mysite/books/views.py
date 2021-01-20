import logging
from django.shortcuts import render
from django.views import View
from books.models import MultiTableManagement
from django.shortcuts import render, HttpResponse, redirect, reverse
# Create your views here.
from books.models import *


def database(request):
    MultiTableManagement().run()
    return HttpResponse('Database Management: Multi Table Management')


class BookSystemAjax(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book_system_ajax.html', {'books': books})

    def post(self, request):
        return HttpResponse('hello')


class DeleteBook(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        logging.warning('Received Get Data: {}'.format(request.GET))
        id = int(request.GET['id'][0])
        Book.objects.get(id=id).delete()
        return HttpResponse('Success!')

    def post(self, request):
        pass
