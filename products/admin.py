from django.contrib import admin
from .models import Product, Category, Age_group, Topic

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Age_group)
admin.site.register(Topic)