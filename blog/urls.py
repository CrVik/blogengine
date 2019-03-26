from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path('', login_required(PostListView.as_view()), name='posts_list_url'),
    path('post/create/', login_required(PostCreateView.as_view()), name='post_create_url'),
    path('post/<int:pk>/', login_required(PostDetailView.as_view()), name='post_detail_url'),
    path('post/<int:pk>/update/', login_required(PostUpdateView.as_view()), name='post_update_url'),
    path('post/<int:pk>/delete/', login_required(PostDeleteView.as_view()), name='post_delete_url'),

    path('users_blogs/',  login_required(BlogListView.as_view()), name='users_blog_list_url'),
    path('user_blogs/subcribe/<int:blog_id>', subcribe, name='subscribe_url'),

    path('users_news/',  login_required(NewsListView.as_view()), name='users_news_list_url'),
    path('users_news/read_post/<int:post_id>', mark_read, name='read_post_url'),

    path('logout', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('login', LoginView.as_view(), {'next_page': settings.LOGIN_REDIRECT_URL}, name='login'),

]
