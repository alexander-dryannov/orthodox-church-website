from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('homepage.urls', namespace='homepage')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('news/', include('blog.urls', namespace='blog')),
    path('about/', include('about.urls', namespace='about')),
    path('schedule/', include('schedule.urls')),
    path('search/', include('search.urls')),
    path('library/', include('reading.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
        )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
        )
