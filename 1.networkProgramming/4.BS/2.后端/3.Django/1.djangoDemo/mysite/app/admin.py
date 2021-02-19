from django.contrib import admin

# Register your models here.
from app import models


class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', "title", 'menus']
    list_editable = [ 'url', "title", 'menus']


class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', "title"]
    list_editable = [ 'url', "title"]


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', "password", "hobby", "normal"]
    list_editable = [ 'username', "password", "hobby", "normal"]


class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = [ 'name']


admin.site.register(models.UserInfo,UserInfoAdmin)
admin.site.register(models.Permission, PermissionAdmin)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.Menu, MenuAdmin)
