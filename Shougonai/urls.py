from django.urls import path
from .views import ( BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView,
)

urlpatterns= [
    path('post/<int:pk>/delete/',
        BlogDeleteView.as_view(), name='post_delete'),
    path('posts/<int:pk>/edit/',
         BlogUpdateView.as_view(), name='post_edit'),
    path('posts/new/', BlogCreateView.as_view(), name='post_new'),
    path('posts/<int:pk>/', BlogDetailView.as_view(),
    name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]