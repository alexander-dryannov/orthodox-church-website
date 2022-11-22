from .forms import BookForm
from django.urls import reverse_lazy
from .models import Book, Chapter
from django.shortcuts import HttpResponse
from .handlers import convert_txt_to_dict
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
    )


class BookListView(ListView):
    model = Book
    queryset = Book.objects.all().filter(is_visible=True)
    context_object_name = 'books'
    template_name = 'book/list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.get_object()
        context['detail'] = True
        context['chapters'] = Chapter.objects.filter(book=self.object.id)
        return context
        return context


class BookCreateView(LoginRequiredMixin, FormView):
    form_class = BookForm
    template_name = 'book/create.html'
    success_url = reverse_lazy('reading:books')
    raise_exception = True

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        book = convert_txt_to_dict(request.FILES.get('file'))
        if form.is_valid():
            is_visible = form.cleaned_data['is_visible']
            book_obj = Book.objects.create(
                title=book['book_title'], is_visible=is_visible)
            for content in book['body']:
                for chapter, text in content.items():
                    text = [t for t in text]
                    Chapter.objects.create(
                        book=book_obj, chapter=chapter, text=''.join(text))
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'book/update.html'
    fields = '__all__'
    raise_exception = True


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book/delete.html'
    success_url = reverse_lazy('books')
    raise_exception = True


class ChapterDetailView(DetailView):
    model = Chapter
    template_name = 'chapter/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.get_object()
        context['detail'] = True
        return context


class ChapterUpdateView(LoginRequiredMixin, UpdateView):
    model = Chapter
    template_name = 'chapter/update.html'
    fields = '__all__'
    raise_exception = True


class ChapterDeleteView(LoginRequiredMixin, DeleteView):
    model = Chapter
    template_name = 'chapter/delete.html'
    success_url = reverse_lazy('books')
    raise_exception = True
