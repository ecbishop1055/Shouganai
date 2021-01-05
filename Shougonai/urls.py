from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns= [
    path('posts/<int:pk>/', BlogDetailView.as_view(),
    name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]