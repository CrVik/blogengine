from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from .models import Blog, Profile, Post


@receiver(user_logged_in, sender=User)
def after_create_user(sender, **kwargs):
    """ This signal create default Blog and Profile for user """

    user = kwargs['request'].user
    try:
        Blog.objects.get(user=user)
    except Blog.DoesNotExist:
        Blog.objects.create(user=user)

    try:
        Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        Profile.objects.create(user=user)


@receiver(post_save, sender=Post)
def send_mail_after_new_post(sender, created,  **kwargs):
    if created:
        users_email = Profile.objects.filter(subscription_blog = kwargs['instance'].blog).values_list('user__email', flat=True)
        user_name = kwargs['instance'].blog.user

        current_site = get_current_site(request=None)
        domain = current_site.domain
        protocol = "http"
        link = kwargs['instance'].get_absolute_url()
        link = f'{protocol}://{domain}{link}'

        send_mail(
                    f'Новый пост в блоге пользователя {user_name}',
                    f'Ссылка на пост: {link}',
                    'qwertyranter@gmail.com',
                    users_email,
                    fail_silently = False,
                )


