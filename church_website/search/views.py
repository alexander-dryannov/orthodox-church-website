from django.db.models import Q
from django.shortcuts import render
from blog.models import Post, Tag


def search(request):
    post_objects = Post.objects.all().filter(is_visible=True)
    tag_objects = Tag.objects.all().filter(is_visible=True)

    search_query = request.GET.get('search', None)
    posts = post_objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    tags = tag_objects.filter(Q(tag__icontains=search_query))
    return render(request, 'search.html', context={'posts': posts, 'tags': tags})
