from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['title', 'is_visible']
        exclude = ['slug']

    file = forms.FileField(widget=forms.ClearableFileInput(), localize=True)
    file.label = 'Файл с расписанием'
