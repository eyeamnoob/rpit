# Generated by Django 3.2.5 on 2021-09-18 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0008_alter_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
        migrations.CreateModel(
            name='LikeActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.ManyToManyField(default=None, help_text='تعداد افرادی که این پست را پسندیده اند', related_name='likeActivity', related_query_name='likeActivity', through='post.LikeActivity', to=settings.AUTH_USER_MODEL, verbose_name='پسند'),
        ),
    ]
