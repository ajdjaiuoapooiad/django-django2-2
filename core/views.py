from django.shortcuts import redirect, render

from core.forms import CreateForm
from core.models import Post


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
    
    context={
        'p': post,
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