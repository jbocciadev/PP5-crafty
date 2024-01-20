from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Topic, Age_group

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    query = None
    categories = None
    age_group = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__friendly_name'
            
            if sortkey == 'age':
                sortkey = 'age_group'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect (reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query)
            print(queries)
            products = products.filter(queries)


        compound_q = Q()

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            if len(categories) == 1:
                compound_q &= Q(category__name__iexact=categories[0])
            else:
                compound_q &= Q(category__name__in=categories)
            
            categories = Category.objects.filter(name__in=categories)
        
        if 'age_group' in request.GET:
            age_group = request.GET['age_group']
            compound_q &= Q(age_group__name__iexact=age_group)
        
        # print(compound_q)
        products = products.filter(compound_q)   


    current_sorting = f'{sort}_{direction}'
    # print(categories[0])

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'age_groups': age_group,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)