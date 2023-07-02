from django.urls import path
from .views import LikeListAPIView, LikeDetailAPIView, PostListAPIView, PostDetailsAPIView


# creating router  
urlpatterns = [
    
    path('posts/', PostListAPIView.as_view(), name='user-list'),
    path('posts/<int:pk>/', PostDetailsAPIView.as_view(), name='user-detail'),
    path('likes/', LikeListAPIView.as_view(), name='user-list'),
    path('likes/<int:pk>/', LikeDetailAPIView.as_view(), name='user-detail'),
]
