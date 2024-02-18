import uuid
from django.urls import path
from profiles import views
from . import views

urlpatterns = [
    path('', views.submit_contact, name="submit_contact"),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('unsubscribe/', views.unsubscribe, name="unsubscribe"),

    path('unsubscribe/<uuid:subscriber_id>/',
         views.unsubscribe, name="unsubscribe"),
]
