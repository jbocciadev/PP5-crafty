from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import QueryDict, HttpResponseRedirect


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
            recipients = [user.email, settings.DEFAULT_SUPPORT_EMAIL]
            email_subject = f"Your contact request - {contact.subject}"
            email_body = f""" Below is a copy of your contact query: \n
    {contact.contact_text}"""
            
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                recipients,
            )

    return redirect(reverse('profile'))


def subscribe(request):
    # https://stackoverflow.com/questions/29492894/how-to-remove-key-from-request-querydict-in-django
    # Cleaning-up the form to get rid of the next field and create new entry in subscribers table
    query = QueryDict.copy(request.POST)
    next = query.pop('next', '/')[0]

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        # Check if email is already subscribed.
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, f"It seems {email} is already subscribed to our Newsletter.")
        else:
            form = SubscriberForm(query)
            if form.is_valid():
                form.save()
                uuid = Subscriber.objects.get(email=email).subscriber_id
                messages.success(request, f""" Subscribed successfully!\n
                            A confirmation email has been sent to {email} """)

                # Send confirmation email
                recipients = [email, settings.DEFAULT_SUPPORT_EMAIL]
                email_subject = f""" Newsletter subscription confirmation for {email} """
                email_body = f""" Hi there!\n
                This is a confirmation email for {email}. 
                You have subscribed to Crafty's newsletter.\n
                If you wish to unsubscribe, please follow the url below:\n
                https://pp5-crafty-015973d8fb4f.herokuapp.com/contact/unsubscribe/{uuid}/ \n
                Regards,\n
                The Crafty team """

                send_mail(
                    email_subject,
                    email_body,
                    settings.DEFAULT_FROM_EMAIL,
                    user_email,
                )

    return HttpResponseRedirect(next)
# https://stackoverflow.com/questions/35796195/how-to-redirect-to-previous-page-in-django-after-post-request


def unsubscribe(request, subscriber_id):
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        subscriber_id = request.POST.get('subscriber_id')
        print(email)
        print(subscriber_id)
        # check that email and subscriber_id both match the record in the database
        if Subscriber.objects.filter(email=email, subscriber_id=subscriber_id).exists():
            Subscriber.objects.filter(email=email, subscriber_id=subscriber_id).delete()
            messages.success(request, "You have successfully unsubscribed!")
        else:
            messages.error(request, f"There seems to be a problem with the details you have provided.")
        return redirect(reverse('products'))
    else:
        context = {
            'subscriber_id': subscriber_id,
        }
    return render(request, 'contact/unsubscribe.html', context)

def unsubscribe_blank(request):
    return redirect(reverse('products'))
