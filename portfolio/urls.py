from django.contrib import admin
from django.urls import path,include # include i write
from django.conf import settings#
from django.conf.urls.static import static#
from jeet import views#

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jeet.urls')),  # Include URLs from the jeet app
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
