from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Posts, Profile
from django.contrib.auth.models import User
from accounts.models import CustomUser
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
    fields = ['title', 'post_image', 'body']

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

class view_profile(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'

class Users_View(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'profiles.html'

    def get_context_data(self,**kwargs):
        context = super(Users_View,self).get_context_data(**kwargs)
        context['object_list'] = CustomUser.objects.all()
        return context
    