# Generated by Django 3.2.5 on 2021-09-16 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20210915_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', related_query_name='comment', to='post.post', verbose_name='پست'),
        ),
    ]