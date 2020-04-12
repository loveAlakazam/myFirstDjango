from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import redirect, render, get_object_or_404 #라이브러리 추가
from .forms import PostForm

def post_list(request):
    posts= Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post= get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    form=PostForm(request.POST)
    if form.is_valid():
        post=form.save(commit=False)        # 아직 저장하지 않은 상태
        post.author=request.user            # 작성자 등록
        post.publised_date=timezone.now()   # published_date 날짜 등록
        post.save()                         # author, publised_date 가 등록후에 저장.
        return redirect('post_detail', pk=post.pk) # post_detail 페이지로 간다.
    else:
        form=PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})


def post_edit(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        form= PostForm(request.POST, instance=post) # PostForm(request.POST, instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})
