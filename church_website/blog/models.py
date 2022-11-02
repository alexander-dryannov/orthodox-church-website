from uuid import uuid4
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class BaseModel(models.Model):
    slug = models.SlugField(unique=True, max_length=42, blank=True)
    created_at = models.DateTimeField('Дата и время создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата и время обновления', auto_now=True)
    is_visible = models.BooleanField('Видимость', default=True)

    def save(self, *args, **kwargs):
        x = 100/0
        if not self.id:
            self.slug = uuid4().hex
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField('Заглавие', max_length=100)
    content = RichTextUploadingField('Контент')
    description = models.TextField('Текст')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts', verbose_name='Теги')

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug, ])

    def get_update_url(self):
        return reverse('blog:post_update', args=[self.slug, ])

    def get_delete_url(self):
        return reverse('blog:post_delete', args=[self.slug, ])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Tag(BaseModel):
    tag = models.CharField('Тег', max_length=100)

    def get_absolute_url(self):
        return reverse('blog:tag_detail', args=[self.slug, ])

    def get_update_url(self):
        return reverse('blog:tag_update', args=[self.slug, ])

    def get_delete_url(self):
        return reverse('blog:tag_delete', args=[self.slug, ])

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
