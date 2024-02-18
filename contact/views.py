from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


from .models import Contact, Subscriber
from .forms import ContactForm, SubscriberForm


@login_required
def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            # print("form is valid")
            contact = form.save(commit=False)
            user = get_object_or_404(User, pk=request.user.id)
            contact.user = user
            contact.save()
            messages.success(request,
                             """Your query has been sent. 
                             You should receive a confirmation email
                             and our staff will be in contact soon.""")
            # Send confirmation email
            user_email = [user.email]
            email_subject = f"Your contact request - {contact.subject}"
            email_body = f""" Below is a copy of your contact query: \n
    {contact.contact_text}"""
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                user_email,
            )

    return redirect(reverse('profile'))


def subscribe(request):
    next = request.POST.get('next', '/')

    if request.method == 'POST':
        email = request.POST.get('email',).lower()
        form = SubscriberForm(email)
        if form.is_valid():
            form.save
            messages.info(request, """ Subscribed successfully!\n 
                          A confirmation email has been sent to {email}. """)

    return (next)


# https://stackoverflow.com/questions/35796195/how-to-redirect-to-previous-page-in-django-after-post-request