from django.contrib import admin
from django.urls import path, include
from . import views

# from .views import PostUpdateView, PostListView, UserPostListView

urlpatterns = [
    path('login/', views.sign_in_view, name='login')
]
