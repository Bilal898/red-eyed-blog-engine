from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from .utils import DetailObjectMixin
# Create your views here.


class PostDetail(DetailObjectMixin, View):
    model = Post
    template = 'blog/post_detail.html'


def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/posts_list.html', context)


def tags_list(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags
    }
    return render(request, 'blog/tags_list.html', context)

class TagDetail(DetailObjectMixin, View):
    model: Tag
    template: 'blog/tag_detail.html'
