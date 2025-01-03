from multiprocessing import context
from django.shortcuts import redirect, render

from core.forms import CommentForm, CreateForm
from core.models import Comment, Like, Post


def index(request):
    posts=Post.objects.all()
    
    context={
        'posts': posts,
    }
    return render(request,'core/index.html',context)

def create(request):
    if request.method == 'POST':
        form=CreateForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form=CreateForm()
        
    context={
        'form': form,
    }
    return render(request,'core/create.html',context)

def detail(request,pk):
    post=Post.objects.get(pk=pk)
    like_count=Like.objects.filter(post=post).count()
    comments=Comment.objects.filter(post=post)
        
        
    context={
        'p': post,
        'like_count': like_count,
        'comments': comments,
    }
    return render(request,'core/detail.html',context)

def update(request,pk):
    post=Post.objects.get(pk=pk)
    form=CreateForm(instance=post)
    if request.method == 'POST':
        form=CreateForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=CreateForm(instance=post)
        
    context={
        'form': form,
    }
    return render(request,'core/update.html',context)


def delete(request,pk):
    post=Post.objects.get(pk=pk)
    post.delete()
    return redirect('index')

def like(request,pk):
        user=request.user
        post=Post.objects.get(pk=pk)
        like=Like.objects.filter(user=user,post=post)
        if like.exists():
            like.delete()
        else:
            like.create(user=user,post=post)
    
        return redirect('index')
    
def comment(request,pk):
    post=Post.objects.get(pk=pk)
    
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.user=request.user
            comment.post=post
            comment.save()
            return redirect('index')
    else:
        form=CommentForm()
    
    context={
        'form': form,
    }
    return render(request,'core/comment.html',context)
    
    
    
