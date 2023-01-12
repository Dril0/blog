from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class BlogListView(ListView):  # Lista todos los Blog.
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):  # detalle de todos los Blog.
    model = Post
    template_name = "post_detail.html"
