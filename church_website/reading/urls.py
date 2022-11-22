from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
    ChapterDetailView,
    ChapterUpdateView,
    ChapterDeleteView
    )


app_name = 'reading'

urlpatterns = [
     path('books/',
          BookListView.as_view(), name='books'),
     path('book/create',
          BookCreateView.as_view(), name='book_create'),
     path('book/<slug:slug>',
          BookDetailView.as_view(), name='book_detail'),
     path('book/<slug:slug>/update',
          BookUpdateView.as_view(), name='book_update'),
     path('book/<slug:slug>/delete',
          BookDeleteView.as_view(), name='book_delete'),
     path('chapter/<slug:slug>',
          ChapterDetailView.as_view(), name='chapter_detail'),
     path('chapter/<slug:slug>/update',
          ChapterUpdateView.as_view(), name='chapter_update'),
     path('chapter/<slug:slug>/delete',
          ChapterDeleteView.as_view(), name='chapter_delete'),
]
