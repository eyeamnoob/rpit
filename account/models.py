from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator

# Create your models here.

class User (AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        verbose_name='لقب',
        unique=True,
        max_length=150,
        validators=[username_validator],
        help_text=' حداکثر تعداد کاراکتر 150 است. فقط میتوانید از اعداد، حروف، @، .، +، -، _ استفاده کنید',
        error_messages={
            'unique': 'کاربر با این لقب وجود دارد',
            'blank': 'این فیلد اجباریست',
        },
    )
    first_name = models.CharField(
        verbose_name='نام',
        max_length=150,
        error_messages={'blank': 'این فیلد اجباریست'},
    )
    last_name = models.CharField(
        verbose_name='نام خانوادگی',
        max_length=150,
        error_messages={'blank': 'این فیلد اجباریست'},
    )
    email = models.EmailField(
        verbose_name='ایمیل',
        validators=[EmailValidator()],
        error_messages={'blank': 'این فیلد اجباریست'},
    )
    is_vip = models.BooleanField(
        verbose_name='ویژه',
        blank=True,
        default=False,
    )

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'