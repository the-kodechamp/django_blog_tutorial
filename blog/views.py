from django.shortcuts import render
from django.views import generic
from .models import Post


"""
Create your views here
A view in Django  is just a Python function that receives 
a web request and returns a web response. 
"""


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'  # a list of all posts will be displayed on index.html


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # detail about each blog post will be on post_detail.html


