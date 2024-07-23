from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils.timezone import now


def index(request):
    posts = Post.objects.select_related(
        'author', 'category', 'location',
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lt=now(),
    )[:5]
    return render(request, 'blog/index.html', context={'post_list': posts})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post.objects.select_related(
            'author', 'category', 'location',
        ).filter(
            is_published=True,
            pub_date__lte=now(),
            category__is_published=True
        ),
        id=post_id,
    )
    return render(request, 'blog/detail.html', context={'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True
    )
    posts = Post.objects.select_related(
        'author', 'category', 'location',
    ).filter(
        category=category,
        is_published=True,
        pub_date__lte=now()
    ).order_by('-pub_date')
    return render(
        request,
        'blog/category.html',
        context={'category': category, 'post_list': posts}
    )
