from django.urls import path
from profiles import views
from . import views

urlpatterns = [
    path('', views.submit_contact, name="submit_contact"),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('unsubscribe/',
         views.unsubscribe, name="unsubscribe"),
]
