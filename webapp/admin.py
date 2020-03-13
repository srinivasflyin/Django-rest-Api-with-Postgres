from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import customuser, airlines,author,cookbook;

admin.site.register(author);
admin.site.register(airlines);
admin.site.register(cookbook);
admin.site.register(customuser, UserAdmin)