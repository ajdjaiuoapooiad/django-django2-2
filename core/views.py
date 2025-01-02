from multiprocessing import context
from django.shortcuts import redirect, render

from core.forms import CreateForm
from core.models import Like, Post


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
        
    context={
        'p': post,
        'like_count': like_count,
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
    
     
