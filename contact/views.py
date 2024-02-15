from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Contact
from .forms import ContactForm


@login_required
def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            user = get_object_or_404(User, pk=user.id)
            contact.user = user
            contact.save()
            messages.success(request, "Your query has been sent. You should receive a confirmation email and our staff will be in contact soon.")

    return render(request, 'profile')
