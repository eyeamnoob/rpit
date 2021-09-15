# Generated by Django 3.2.5 on 2021-09-15 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20210915_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', related_query_name='comment', to='post.comment', verbose_name='در پاسخ به'),
        ),
    ]
