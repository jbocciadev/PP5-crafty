from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import handler404, handler500


# Uncomment lines 11, 12, and 22 to test server error 500 page. Navigate to
# https://pp5-crafty-015973d8fb4f.herokuapp.com/500
# def view_500(request):
#     raise Exception("Test error 500")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    # path('500/', view_500),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'crafty.views.handler404'

handler500 = 'crafty.views.handler500'
