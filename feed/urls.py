from django.contrib import admin
from django.urls import path, include
from . import views

# from .views import PostUpdateView, PostListView, UserPostListView

urlpatterns = [
    path('', views.get_routes, name='get_routes')
]