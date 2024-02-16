from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order
from contact.models import Contact
from contact.forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def profile(request):
    """ Display the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    userdetails = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           "Update failed. Please ensure all fields on the form are valid.")
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    contacts = Contact.objects.filter(user=request.user).order_by('-date_submitted')
    contact_form = ContactForm()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'user': userdetails,
        'contacts': contacts,
        'contact_form': contact_form,
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
