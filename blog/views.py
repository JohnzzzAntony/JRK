from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def post_list(request):
    """Image: Shows Blog post cards in a grid with pagination."""
    post_list = Post.objects.filter(is_published=True).order_by('-created_at')
    paginator = Paginator(post_list, 6) # 6 posts per page for 3x2 grid
    
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    """Individual Blog post view with Hero Title."""
    post = get_object_or_404(Post, slug=slug, is_published=True)
    return render(request, 'blog/post_detail.html', {'post': post})
