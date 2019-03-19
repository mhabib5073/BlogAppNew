from django.urls import path
from .views import PostListView,PostDetail,PostCreat,PostUpdate,PostDelete,UserPostList
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('user/<str:username>',UserPostList.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetail.as_view(),name='post-detail'),
    path('post/new/',PostCreat.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdate.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDelete.as_view(),name='post-delete'),
    path('about/', views.about,name='blog-about'),
]
