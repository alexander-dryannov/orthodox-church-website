from blog.models import Post
from django.shortcuts import render


def home_page(request):
    posts = Post.objects.all().filter(is_visible=True).order_by('-pk')[:7]
    return render(request, 'home.html', context={'posts': posts})
