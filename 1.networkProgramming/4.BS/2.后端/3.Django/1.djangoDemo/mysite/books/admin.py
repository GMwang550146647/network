from django.contrib import admin

# Register your models here.
from books import models

admin.site.register(models.Author)
admin.site.register(models.AuthorDetail)
admin.site.register(models.Book)
admin.site.register(models.Publish)
admin.site.register(models.Book_Author)
