from django import template
from blog.models import Profile, Post

register = template.Library()


@register.simple_tag
def stats(blog_id, user):
    user_subscribe = Profile.objects.filter(user=user, subscription_blog__id=blog_id).count()
    count_blog_post = Post.objects.filter(blog_id=blog_id).count()
    return {'user_subscribe': user_subscribe, 'count_blog_post': count_blog_post}


@register.simple_tag
def is_read_post(post_id, user):
    return Profile.objects.filter(user=user, subscription_blog__profile__is_read_post__id = post_id).count()
