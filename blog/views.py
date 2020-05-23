from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from .utils import DetailObjectMixin, CreateObjectMixin
from .forms import TagForm, PostForm
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
    model = Tag
    template = 'blog/tag_detail.html'

class TagCreate(CreateObjectMixin, View):
    model = TagForm
    template = 'blog/tag_create.html'

class PostCreate(CreateObjectMixin, View):
    model = PostForm
    template = 'blog/post_create.html'

class TagUpdate(View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        context = {
            'form': bound_form,
            'tag': tag
        }
        return render(request, 'blog/tag_update.html', context)

    def post(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        bound_form = TagForm(request.POST, instance=tag)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)

        context = {
            'form': bound_form,
            'tag': tag
        }
        return render(request, 'blog/tag_update.html', context)
