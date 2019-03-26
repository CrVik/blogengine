from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post, Blog, Profile


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(blog__user=self.request.user)


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        user = self.request.user
        user_blog = Blog.objects.get(user=user)

        form.instance.blog = user_blog
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    template_name = 'blog/post_create.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog_list'

    def get_queryset(self):
        return Blog.objects.exclude(user=self.request.user)

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     # context['book_list'] = Book.objects.all()
    #     return context


class NewsListView(ListView):
    model = Post
    template_name = 'blog/news_list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        user_profile = Profile.objects.get(user = self.request.user)
        subscibed_blogs = user_profile.subscription_blog.all()
        return Post.objects.filter(blog__in=subscibed_blogs)


def subcribe(request, blog_id):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    blog = Blog.objects.get(pk=blog_id)
    if Profile.objects.filter(user=user, subscription_blog=blog):
        user_profile.subscription_blog.remove(blog)
    else:
        user_profile.subscription_blog.add(blog)

    return redirect('users_blog_list_url')


def mark_read(request, post_id):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    post = Post.objects.get(pk=post_id)
    if Profile.objects.filter(user=user, is_read_post=post):
        user_profile.is_read_post.remove(post)
    else:
        user_profile.is_read_post.add(post)

    return redirect('users_news_list_url')
