from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Posts
# Create your views here.
class BlogListView(LoginRequiredMixin, ListView):
    model = Posts
    template_name = 'home.html'

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Posts
    template_name = 'post_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = 'post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form): 
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user