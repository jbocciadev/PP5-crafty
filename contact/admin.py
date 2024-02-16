from django.contrib import admin
from .models import Contact

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


admin.site.register(Contact, ContactAdmin)


# https://earthly.dev/blog/customize-django-admin-site/