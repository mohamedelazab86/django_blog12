from django.shortcuts import render
from .models import Post
# create crud by class based view
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

class List_post(ListView):
    model=Post
    
class Detail_post(DetailView):
    model=Post

class Create_post(CreateView):
    model=Post
    fields='__all__'
    success_url='/posts/'
    template_name='posts/create.html'

class Update_post(UpdateView):
    model=Post
    fields="__all__"
    template_name='posts/update.html'

class Delete_post(DeleteView):
    model=Post
    success_url='/posts/'
    template_name='posts/delete.html'