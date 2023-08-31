from django.contrib import admin

from .models import Users, Category, Brand, Product

admin.site.register([Users, Category, Brand, Product])
