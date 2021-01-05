from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Posts
# Create your views here.
class BlogListView(ListView):
    model = Posts
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Posts
    template_name = 'post_detail.html'