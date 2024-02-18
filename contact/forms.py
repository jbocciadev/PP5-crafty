from django import forms
from .models import Contact, Subscriber

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = (
            'subject',
            'contact_text',
        )

class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = (
            'email',
        )
