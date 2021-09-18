from django.db import models
from django.db.models.fields import related
from account.models import User
from django.shortcuts import get_object_or_404
import datetime
from django.contrib.auth import get_user, get_user_model
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
        upload_to='%y/%m/%d',
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
    like = models.ManyToManyField(
        get_user_model(),
        through='likeactivity',
        related_name='liked_posts',
        related_query_name='liked_posts',
        verbose_name='پسند',
        default=None,
        help_text='تعداد افرادی که این پست را پسندیده اند',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        related_name='post',
        related_query_name='post',
        verbose_name='کاربر'
    )
    date = models.DateTimeField(
        auto_now=True,
        verbose_name='تاریخ'
    )

    def __str__(self) -> str:
        return str(self.title) + " - " + str(self.body[0:15]) + '...'
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None) -> None:
        try:
            obj = get_object_or_404(Post, pk=self.pk)
            obj.image.delete()
        except:
            pass
        if self.image:
            self.image.name = str(self.user.pk) + "_" + str(self.user.get_username()) + '_' + datetime.datetime.now().strftime("%y-%m-%d-%H-%M") + '.' + self.image.name.split('.')[-1]
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        return super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'
        ordering = ['-date']


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(),
        on_delete=models.CASCADE,
        related_name='comment',
        related_query_name='comment',
        verbose_name='کاربر',
        blank=True
    )
    body = models.CharField(
        max_length=150,
        verbose_name='نظر'
    )
    reply_to = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name='در پاسخ به',
        related_name='comment',
        related_query_name='comment',
        blank=True,
        null=True
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comment',
        related_query_name='comment',
        verbose_name='پست',
    )

    def __str__(self) -> str:
        return str(self.user) + ': ' + str(self.body[0:10]) + '...'
    
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظر ها'
        ordering = ['-date']
    

class LikeActivity(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now=True
    )

    def __str__(self) -> str:
        return str(self.user.get_username()) + ' liked ' + str(self.post.title)
    
    class Meta:
        ordering = ['-date']