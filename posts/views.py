from django.shortcuts import render,redirect
from .models import Post,Comment
from .forms import PostForm,CommentForm

# Create your views here.


# c =============== create crud opertions by function based view ===============

def list_post(request):
    posts=Post.objects.all()
    context={'post_list':posts}
    return render(request,'posts/post_list.html',context)

def detail_post(request,pk):
    post=Post.objects.get(id=pk)
    comment=Comment.objects.filter(post=post)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.post=post
            my_form.save()
            #return redirect('/details/{{post.id}}')
    else:


        form=CommentForm()
    context={
        'post':post,
        'comment':comment,
        'form':form

        }
    return render(request,'posts/post_detail.html',context)

def create_post(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.author=request.user
            my_form.save()
            return redirect('/posts/')
    else:

           
         form=PostForm()
    context={'form':form}
    return render(request,'posts/create.html',context)

def update_post(request,pk):
    post=Post.objects.get(id=pk)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.author=request.user
            my_form.save()
            return redirect('/posts/')
    else:
    
        form=PostForm(instance=post)
    context={'form':form}
    return render(request,'posts/update.html',context)
def delete_post(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/')