from django.shortcuts import redirect, render

from core.forms import CreateForm


def index(request):
    return render(request,'core/index.html')

def create(request):
    if request.method == 'POST':
        form=CreateForm(request.POST)
        if form.is_valide():
            post=form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form=CreateForm()
    context={
        'form': form,
    }
    return render(request,'core/create.html',context)