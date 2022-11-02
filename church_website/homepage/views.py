from django.views.generic import ListView
from blog.models import Post
from django.shortcuts import render


# class HomePage(ListView):
#     template_name = 'home.html'
#     # context_object_name = 'albums'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts'] = Post.objects.all().filter(is_visible=True).order_by('-pk')[:4]
#         return context


def home_page(request):
    posts = Post.objects.all().filter(is_visible=True).order_by('-pk')[:7]
    return render(request, 'home.html', context={'posts': posts})
