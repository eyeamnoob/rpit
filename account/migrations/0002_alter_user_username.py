# Generated by Django 3.2.5 on 2021-07-28 07:13

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'blank': 'این فیلد اجباریست', 'unique': 'کاربر با این لقب وجود دارد'}, help_text=' حداکثر تعداد کاراکتر 150 است. فقط میتوانید از اعداد، حروف، @، .، +، -، _ استفاده کنید', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='لقب'),
        ),
    ]
