from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Topic, Age_group

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    query = None
    categories = None
    age_group = None

    if request.GET:

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect (reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            print(queries)
            products = products.filter(queries)

        else:

            q = Q()

            if 'category' in request.GET:
                categories = request.GET['category'].split(',')
                if len(categories) == 1:
                    q &= Q(category__name__iexact=categories[0])
                else:
                    q &= Q(category__name__in=categories)
            
            if 'age_group' in request.GET:
                age_group = request.GET['age_group']
                q &= Q(age_group__name__iexact=age_group)
            
            print(q)
            products = products.filter(q)        

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'age_groups': age_group
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)