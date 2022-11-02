from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'is_visible', 'cover']
        exclude = ['slug']

    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple':True})
        )
