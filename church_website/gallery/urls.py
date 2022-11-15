from django.urls import path
from .views import (
    AlbumListView,
    AlbumCreateView,
    AlbumDetailView,
    AlbumUpdateView,
    AlbumDeleteView,
    AlbumImageDetailView,
    )

from .views import rotate_image


app_name = 'gallery'

urlpatterns = [
     path('albums/',
          AlbumListView.as_view(), name='albums'),
     path('album/create',
          AlbumCreateView.as_view(), name='album_create'),
     path('album/<slug:slug>',
          AlbumDetailView.as_view(), name='album_detail'),
     path('album/<slug:slug>/update',
          AlbumUpdateView.as_view(), name='album_update'),
     path('album/<slug:slug>/delete',
          AlbumDeleteView.as_view(), name='album_delete'),
     path('image/<slug:slug>',
          AlbumImageDetailView.as_view(), name='image_detail'),

     path('image/<slug:slug>/rotate', rotate_image, name='rotate')
]
