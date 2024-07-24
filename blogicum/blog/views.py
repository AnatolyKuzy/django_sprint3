from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from django.conf import settings

from .models import Post, Category


def get_published_posts(request, **filters):
    return Post.objects.select_related(
        'author', 'category', 'location',
    ).filter(
        category__is_published=True,
        is_published=True,
        pub_date__lt=now(),
        **filters
    )


def index(request):
    posts = get_published_posts(request)[:settings.NUMBER_OF_POSTS]
    return render(request, 'blog/index.html', context={'post_list': posts})


def post_detail(request, post_id):
    posts = get_object_or_404(
        get_published_posts(request),
        id=post_id,
    )
    return render(request, 'blog/detail.html', context={'post': posts})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    posts = get_published_posts(
        request, category=category
    )
    return render(
        request,
        'blog/category.html',
        context={'category': category, 'post_list': posts}
    )
