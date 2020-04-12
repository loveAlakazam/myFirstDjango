from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404 #라이브러리 추가

def post_list(request):
    posts= Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post= get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
