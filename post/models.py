from django.db import models
from account.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='عنوان',
        verbose_name='عنوان'
    )
    image = models.ImageField(
        upload_to='%Y/%M/%D',
        verbose_name='عکس',
        null=True,
        blank=True,
        help_text='عکسی که برای پست نمایش داده میشود'
    )
    body = models.TextField(
        max_length=500,
        verbose_name='متن پست',
        help_text='متن اصلی پست',
    )
    like = models.PositiveBigIntegerField(
        verbose_name='پسند',
        default=0,
        help_text='تعداد افرادی که از این پست خوششان آمده است',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='User',
        related_query_name='User',
        verbose_name='کاربر'
    )
    date = models.DateTimeField(
        auto_now=True,
        verbose_name='تاریخ'
    )

    def __str__(self) -> str:
        return str(self.title) + " - " + str(self.body[0:15]) + '...'
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None) -> None:
        if self.image:
            self.image.name = str(self.pk) + "_" + str(self.user.get_username()) + '.' + self.image.name.split('.')[-1]
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        ordering = ['-date']
