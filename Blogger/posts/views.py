from django.shortcuts import render , redirect
from .models import Post
from django.utils import timezone



# Create your views here.

def home_view(request):

    posts=Post.objects.all()

    return render(request,'posts/home.html',{'posts':posts})

def add_post_view(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        is_published=request.POST.get('is_published') == 'on'
        published_at=request.POST.get('published_at')
        poster = request.FILES.get('poster')   
        if not published_at:
            published_at = timezone.now()

        Post.objects.create(title=title, content=content, is_published=is_published,published_at=published_at,poster=poster)
        return redirect('posts:home_view')

    return render(request,'posts/add_post.html')

def detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/detail.html', {'post': post})

def update_post_view(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.is_published = request.POST.get('is_published') == 'on'
        published_at = request.POST.get('published_at')

        if published_at:
            post.published_at = published_at

        if request.FILES.get('poster'):
            post.poster = request.FILES.get('poster')

        post.save()
        return redirect('posts:detail_view', post_id=post.id)

    return render(request, 'posts/update_post.html', {'post': post})

def delete_post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts:home_view')

