# Generated by Django 4.1.1 on 2022-10-26 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_tag_post_alter_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=1, verbose_name='Текст'),
            preserve_default=False,
        ),
    ]
