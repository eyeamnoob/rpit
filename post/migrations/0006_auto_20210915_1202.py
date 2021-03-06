# Generated by Django 3.2.5 on 2021-09-15 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20210915_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comment', related_query_name='comment', to='post.post', verbose_name='پست'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', related_query_name='comment', to='post.comment', verbose_name='پاسخ'),
        ),
    ]
