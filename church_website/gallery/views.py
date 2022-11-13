import json
from PIL import Image
from pathlib import Path
from .forms import AlbumForm
from django.conf import settings
from django.urls import reverse_lazy
from .models import Album, AlbumImage
from .handlers import create_image_column
from django.shortcuts import HttpResponse
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
    )


@csrf_exempt
def rotate_image(request, slug):
    angle = json.loads(request.body)
    image = AlbumImage.objects.get(slug=slug)
    p = Path(__file__).resolve().parent.parent.joinpath(
        settings.MEDIA_ROOT).joinpath(str(image.src))
    print(p)
    im = Image.open(p)
    e = im.getexif()
    print(e)
    im = im.rotate(angle.get('angle'), expand=True)
    im.save(p)
    return HttpResponse(
        json.dumps({'status': 200}),
        content_type="application/json"
        )


class AlbumListView(ListView):
    model = Album
    queryset = Album.objects.all().filter(is_visible=True)
    context_object_name = 'albums'
    template_name = 'list.html'


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = AlbumImage.objects.filter(album=self.object.id)
        ctx = create_image_column(context['images'])
        context['images'] = ctx
        context['obj'] = self.get_object()
        context['detail'] = True
        return context


class AlbumCreateView(LoginRequiredMixin, FormView):
    form_class = AlbumForm
    template_name = 'create.html'
    success_url = reverse_lazy('gallery:albums')
    raise_exception = True

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('images')
        if form.is_valid():
            name = form.cleaned_data['title']
            is_visible = form.cleaned_data['is_visible']
            cover = form.cleaned_data['cover']
            album_obj = Album.objects.create(
                title=name, is_visible=is_visible, cover=cover
                )
            for file in files:
                AlbumImage.objects.create(
                    album=album_obj, src=file
                    )
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    template_name = 'update.html'
    fields = '__all__'
    raise_exception = True


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'delete.html'
    success_url = reverse_lazy('albums')
    raise_exception = True


class AlbumImageDetailView(DetailView):
    model = AlbumImage
    template_name = 'image_detail.html'
