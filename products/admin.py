from django.contrib import admin
from .models import Product, Category, Age_group, Topic, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'age_group',
        'topic',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'product',
        'rating',
        'review',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Age_group)
admin.site.register(Topic)