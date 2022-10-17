from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = 'Admin Panel'
admin.site.site_header = 'Uchaguzi Online'
admin.site.index_title = 'Welcome back ...'

urlpatterns = [
    path('voters/', include('voters.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
