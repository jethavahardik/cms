from django.urls import path
from .views import (
    UserListAPIView, 
    UserDetailAPIView,
    UserLoginAPIView,
    )

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
]