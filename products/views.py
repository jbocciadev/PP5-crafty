from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile as Profile
from .forms import ProductForm, ProductReviewForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    # Append number of reviews in each product
    for product in products:
        product.num_reviews = Review.objects.filter(product=product).count()

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
            products = products.filter(queries)

        # Compound queryset to accommodate for multiple-categories
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
        
        products = products.filter(compound_q)   

    current_sorting = f'{sort}_{direction}'

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
    # Append number of reviews to product
    product.num_reviews = Review.objects.filter(product=product).count()
    # https://stackoverflow.com/questions/15635790/how-to-count-the-number-of-rows-in-a-database-table-in-django#:~:text=You%20can%20either%20use%20Python's,the%20provided%20count()%20method.&text=You%20should%20also%20go%20through%20the%20QuerySet%20API%20Documentation%20for%20more%20information.
    reviews = Review.objects.filter(product=product)
    
    if request.user.is_authenticated:
        user = request.user
        profile = get_object_or_404(Profile, user=user)

        # check if user has purchased product
        has_purchased = OrderLineItem.objects.filter(order__in=user.user_profile.orders.all()).filter(product=product)
        if has_purchased:
            user.has_purchased = True
        
        # check if user has submitted a review
        try:
            user_review = reviews.get(user=request.user)
        except Review.DoesNotExist:
            user_review = False

        if user_review:
            # review_form = ProductReviewForm(instance=user_review)
            user.review = user_review
        # else:
        #     review_form = ProductReviewForm(instance=product)

    context = {
        'product': product,
        'reviews': reviews,
        'user': user,
        # 'review_form': review_form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
   
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)