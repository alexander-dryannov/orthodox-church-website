from uuid import uuid4
from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    slug = models.SlugField(unique=True, max_length=42, blank=True)
    created_at = models.DateTimeField('Дата и время создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата и время обновления', auto_now=True)
    is_visible = models.BooleanField('Видимость', default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid4().hex
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Book(BaseModel):
    title = models.CharField('Название книги', max_length=100)
    description = models.TextField('Описание', blank=True)

    def get_absolute_url(self):
        return reverse('reading:book_detail', args=[self.slug, ])

    def get_update_url(self):
        return reverse('reading:book_update', args=[self.slug, ])

    def get_delete_url(self):
        return reverse('reading:book_delete', args=[self.slug, ])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Chapter(BaseModel):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='book')
    chapter = models.CharField('Название/Номер главы', max_length=100)
    text = models.TextField('Текст')

    def get_absolute_url(self):
        return reverse('reading:chapter_detail', args=[self.slug, ])

    def get_update_url(self):
        return reverse('reading:chapter_update', args=[self.slug, ])

    def get_delete_url(self):
        return reverse('reading:chapter_delete', args=[self.slug, ])

    def __str__(self):
        return self.chapter

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'
