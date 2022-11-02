from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView
from .views import TagListView, TagDetailView, TagUpdateView, TagDeleteView, TagCreateView

app_name = 'blog'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/update', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete', PostDeleteView.as_view(), name='post_delete'),

    path('tags/', TagListView.as_view(), name='tags'),
    path('tag/create', TagCreateView.as_view(), name='tag_create'),
    path('tag/<slug:slug>', TagDetailView.as_view(), name='tag_detail'),
    path('tag/<slug:slug>/update', TagUpdateView.as_view(), name='tag_update'),
    path('tag/<slug:slug>/delete', TagDeleteView.as_view(), name='tag_delete'),
]
