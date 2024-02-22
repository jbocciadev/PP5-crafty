from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return self.friendly_name

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    age_group = models.ForeignKey('Age_group', null=True, blank=True, on_delete=models.SET_NULL)
    topic = models.ForeignKey('Topic', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def calculate_rating(self, *args, **kwargs):
#     '''Calculating average rating (to be called
#     whenever a new rating is added)'''

        reviews = Review.objects.filter(product=self)
        self.rating = reviews.aggregate(Avg('rating'))['rating__avg']
        self.save()
# https://stackoverflow.com/questions/74116689/how-to-count-reviews-for-a-product-in-django
        


class Age_group(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Topic(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Review(models.Model):
    user = models.ForeignKey(User, null=False,
                             blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False,
                                blank=False, on_delete=models.CASCADE)
    rating_choices=[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    rating = models.IntegerField(choices=rating_choices)
    # rating = models.IntegerField(null=False, blank=False, default=0)
    review = models.TextField(null=False, blank=True, default='')

    def save(self, *args, **kwargs):
        '''Overriding save method to calculate avg rating
        every time a new review is added'''
        super(Review, self).save(*args, **kwargs)
        self.product.calculate_rating(self.product)
