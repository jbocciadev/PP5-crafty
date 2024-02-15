import uuid

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Contact(models.Model):
    case_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, null=False,
                             blank=False, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True, null=True)
    contact_text = models.TextField(blank=False, null=False)
    date_submitted = models.DateTimeField(auto_now_add=True, blank=False, null=False)

# https://docs.djangoproject.com/en/dev/ref/models/fields/#uuidfield
