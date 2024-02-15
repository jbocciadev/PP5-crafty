from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'case_id',
        'date_submitted',
        'user',
        'subject'
        'contact_text'
    )

admin.site.register(Contact, ContactAdmin)
