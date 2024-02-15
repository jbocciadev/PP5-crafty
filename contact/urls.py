from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_contact, name="submit_contact"),
]