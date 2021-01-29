import logging
from django.shortcuts import render
from django.views import View
from books.models import MultiTableManagement
from django.shortcuts import render, HttpResponse, redirect, reverse
# Create your views here.
from books.models import *
from django.core.validators import ValidationError
from django import forms


class BookForm(forms.ModelForm):
    re_title = forms.CharField()

    def __init__(self, *args, **kwargs):  # 批量操作
        super().__init__(*args, **kwargs)
        for field in self.fields:
            # field.error_messages = {'required':'不能为空'} #批量添加错误信息,这是都一样的错误，不一样的还是要单独写。
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Book
        # fields = ['title','price']
        fields = "__all__"  # ['title,'price'] 指定字段生成form
        # exclude=['title',] #排除字段
        labels = {
            "title": "书名",
            "price": "价格"
        }
        error_messages = {
            'title': {'required': '不能为空', }  # 每个字段的错误都可以写
        }

    def clean(self):
        title_value = self.cleaned_data.get('title')
        re_title_value = self.cleaned_data.get('re_title')
        # 1.密码验证 (也可以做很多字符验证...)
        if title_value == re_title_value:
            return self.cleaned_data  # 全局钩子要返回所有的数据
        else:
            self.add_error('re_title', '两次密码不一致')
            # 在re_password这个字段的错误列表中加上一个错误，并且clean_data里面会自动清除这个re_password的值，所以打印clean_data的时候会看不到它
            raise ValidationError('两次密码不一致')


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
        request_html = "{}.html".format(request.GET.get('action', 'add_book'))
        book_id = request.GET.get('id', None)
        book = Book.objects.get(id=book_id) if book_id else {}
        # 普通版本
        if request_html == "add_book.html":
            # 如果是修改，把数据先填好
            # 如果是添加，无数据
            publish_objs = Publish.objects.all()
            author_objs = Author.objects.all()
            data = {
                'book': book,
                'publish_objs': publish_objs,
                'author_objs': author_objs,
            }
        # model form版本（不用自己写表格验证）
        else:
            book = BookForm(instance=book) if book else BookForm()
            data = {
                'book': book,
            }
        return render(request, request_html, data)

    def post(self, request):
        request_url = request.POST.get('action', 'add_book')
        data = request.POST
        book_id = data.get('id', '')
        if request_url == 'add_book':
            if book_id:
                # book_id update
                Book.objects.filter(id=book_id).update(
                    title=data.get('title', 'Error'),
                    publishDate=data.get('publishDate', '2020-01-01'),
                    price=data.get('price', '-1'),
                    publish=Publish.objects.filter(id=data['publish'])[0],
                )
                authors = data.getlist('authors')
                Book.objects.get(id=book_id).author.set(authors)
            else:
                # create
                new_obj = Book.objects.create(
                    title=data.get('title', 'Error'),
                    publishDate=data.get('publishDate', '2020-01-01'),
                    price=data.get('price', '-1'),
                    publish=Publish.objects.filter(id=data['publish'])[0],
                )
                authors = [int(item) for item in data.getlist('authors')]
                new_obj.author.add(*authors)
            return redirect('/book_system_ajax/')
        else:
            ################ orm 版本###############
            # if book_id:
            #     # book_id update
            #     book_form_obj = BookForm(request.POST)
            #     if book_form_obj.is_valid():
            #         book_form_obj.cleaned_data.pop('re_title')
            #         authors = book_form_obj.cleaned_data.pop('author')
            #         Book.objects.filter(id=book_id).update(
            #             **book_form_obj.cleaned_data
            #         )
            #         Book.objects.get(id=book_id).author.set(authors)
            #         return redirect('/book_system_ajax/')
            #     else:
            #         return render(request,'{}.html'.format(request_url),{'book':book_form_obj})
            # else:
            #     # create
            #     book_form_obj = BookForm(request.POST)
            #     if book_form_obj.is_valid():
            #         book_form_obj.cleaned_data.pop('re_title')
            #         authors = book_form_obj.cleaned_data.pop('author')
            #         new_obj = Book.objects.create(
            #             **book_form_obj.cleaned_data
            #         )
            #         new_obj.author.add(*authors)
            #         return redirect('/book_system_ajax/')
            #     else:
            #         return render(request,'{}.html'.format(request_url),{'book':book_form_obj})

            ############Model Form 版本############
            if book_id:
                # book_id update
                book_form_obj = BookForm(request.POST,instance=Book.objects.filter(id=book_id))
                if book_form_obj.is_valid():
                    book_form_obj.save()
                    return redirect('/book_system_ajax/')
                else:
                    return render(request,'{}.html'.format(request_url),{'book':book_form_obj})
            else:
                # create
                book_form_obj = BookForm(request.POST)
                if book_form_obj.is_valid():
                    book_form_obj.save()
                    return redirect('/book_system_ajax/')
                else:
                    return render(request,'{}.html'.format(request_url),{'book':book_form_obj})