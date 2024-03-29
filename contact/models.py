from typing import Any
import uuid

from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    case_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, null=False,
                             blank=False, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True, null=True)
    contact_text = models.TextField(blank=False, null=False)
    date_submitted = models.DateTimeField(auto_now_add=True, blank=False, null=False)

# https://docs.djangoproject.com/en/dev/ref/models/fields/#uuidfield


class Subscriber(models.Model):
    subscriber_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(blank=False, null=False, unique=True)

    def save(self, *args, **kwargs):
        """ Override save method to convert email to lowercase """
        self.email = self.email.lower()
        super(Subscriber, self).save(*args, **kwargs)
