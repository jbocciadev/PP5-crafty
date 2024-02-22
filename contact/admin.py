from django.contrib import admin
from .models import Contact, Subscriber


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'case_id',
        'date_submitted',
        'user',
        'subject',
        'contact_text',
    )
    search_fields = (
        'user',
        'case_id',
    )


class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'subscriber_id',
        'email',
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
