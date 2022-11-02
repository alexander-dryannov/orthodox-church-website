from .models import Post, Tag
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    model = Post
    queryset = Post.objects.all().filter(is_visible=True).order_by('-pk')
    context_object_name = 'posts'
    template_name = 'post/list.html'
    paginate_by = 7

    # def get_queryset(self):
    #     print('Зашел в queryset')
    #     name = self.kwargs.get('name', '')
    #     object_list = self.model.objects.all()
    #     if name:
    #         object_list = object_list.filter(
    #             Q(title__icontains=name) | Q(description__icontains=name)
    #             )
    #         return object_list
    #     return object_list


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.get_object()
        context['detail'] = True
        return context


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post/update.html'
    fields = ['title', 'content', 'description', 'tags', 'is_visible']
    raise_exception = True


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/create.html'
    fields = ['title', 'content', 'description', 'tags', 'is_visible']
    success_url = reverse_lazy('blog:posts')
    raise_exception = True


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('blog:posts')
    raise_exception = True


class TagListView(ListView):
    model = Tag
    queryset = Tag.objects.all().filter(is_visible=True).order_by('-pk')
    context_object_name = 'tags'
    template_name = 'tag/list.html'
    # paginate_by = 5


class TagDetailView(DetailView):
    model = Tag
    template_name = 'tag/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.get_object()
        context['detail'] = True
        return context


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'tag/create.html'
    fields = ['title', 'content', 'description', 'tags', 'is_visible']
    success_url = reverse_lazy('blog:posts')
    raise_exception = True


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    template_name = 'tag/update.html'
    fields = ['tag', 'is_visible']
    raise_exception = True


class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'tag/delete.html'
    success_url = reverse_lazy('blog:tags')
    raise_exception = True
