from django.contrib import admin

# Register your models here.
from app import models


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', "title"]


admin.site.register(models.UserInfo)
admin.site.register(models.Permission,PermissionAdmin)
admin.site.register(models.Role)
