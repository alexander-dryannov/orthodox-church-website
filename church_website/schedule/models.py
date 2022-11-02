from django.db import models
from uuid import uuid4
from django.urls import reverse


class Schedule(models.Model):
    title = models.CharField('Месяц', max_length=99)
    data = models.JSONField()
    slug = models.SlugField(max_length=42, blank=True, unique=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата последнего обновления', auto_now=True)
    is_visible = models.BooleanField('Видимость', default=True)

    def get_absolute_url(self):
        return reverse('schedule:schedule_detail', args=[self.slug, ])

    def get_update_url(self):
        return reverse('schedule:schedule_update', args=[self.slug, ])

    def get_delete_url(self):
        return reverse('schedule:schedule_delete', args=[self.slug, ])

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid4().hex
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
