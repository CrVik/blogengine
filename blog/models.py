# -*- coding: utf-8 -*-


from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db import models


class Blog(models.Model):
    created = models.DateTimeField(auto_now=True, )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Блог пользователя: {self.user}'


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='Блог')
    title = models.CharField(max_length=150, db_index=True, verbose_name='Заоголовок')
    body = models.TextField(verbose_name='Текст публикации')
    date_pub = models.DateTimeField(auto_now_add=True,verbose_name='Дата публикации')

    class Meta :
        ordering = ["-date_pub"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_blog = models.ManyToManyField(Blog, blank=True,  verbose_name='Подписка на блог')
    is_read_post = models.ManyToManyField(Post, blank=True,  verbose_name='Пост прочитан')
