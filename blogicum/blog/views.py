from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils.timezone import now


def get_published_posts(request, **filters):
    posts = Post.objects.select_related(
        'author', 'category', 'location',
    ).filter(
        category__is_published=True,
        is_published=True,
        pub_date__lt=now(),
        **filters
    )
    return posts


def index(request):
    posts = get_published_posts(request)[:5]
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
    ).order_by('-pub_date')
    return render(
        request,
        'blog/category.html',
        context={'category': category, 'post_list': posts}
    )
