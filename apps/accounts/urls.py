from django.urls import path, include
from .views import UserListCreateAPIView, UserDetailAPIView

urlpatterns = [
    path('auth/', include('allauth.urls')), # Social Media login Url
    path('users/', UserListCreateAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]