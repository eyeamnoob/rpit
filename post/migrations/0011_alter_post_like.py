# Generated by Django 3.2.5 on 2021-09-18 08:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0010_alter_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(default=None, help_text='تعداد افرادی که این پست را پسندیده اند', related_name='liked_posts', related_query_name='liked_posts', through='post.LikeActivity', to=settings.AUTH_USER_MODEL, verbose_name='پسند'),
        ),
    ]
