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
        Book.objects.filter(id=id).delete()
        return HttpResponse('Success!')

    def post(self, request):
        pass


class AddBook(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request):
        # 如果是修改，把数据先填好
        # 如果是添加，无数据
        book_id=request.GET.get('id',None)
        book=Book.objects.get(id=book_id) if book_id else {}
        publish_objs=Publish.objects.all()
        author_objs=Author.objects.all()
        data={
            'book':book,
            'publish_objs':publish_objs,
            'author_objs':author_objs,
        }
        return render(request, 'book_add.html',data)

    def post(self, request):
        data = request.POST
        print(data)
        book_id=data.get('id','')
        if book_id:
            #book_id
            Book.objects.filter(id=book_id).update(
                title=data.get('title', 'Error'),
                publishDate=data.get('publishDate', '2020-01-01'),
                price=data.get('price', '-1'),
                publish=Publish.objects.filter(id=data['publish'])[0],
            )
            authors=data.getlist('authors')
            Book.objects.get(id=book_id).author.set(authors)
        else:
            #create
            new_obj=Book.objects.create(
                title=data.get('title','Error'),
                publishDate=data.get('publishDate','2020-01-01'),
                price=data.get('price','-1'),
                publish=Publish.objects.filter(id=data['publish'])[0],
            )
            authors=[int(item) for item in data.getlist('authors')]
            new_obj.author.add(*authors)
        return redirect('/book_system_ajax/')