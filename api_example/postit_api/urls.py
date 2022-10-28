"""api_example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import (PostList,
                    PostDetail,
                    CommentList,
                    PostCommentList,
                    CommentDetail,
                    PostLikeCreate,
                    UserCreate)

urlpatterns = [
    path('posts', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view()),
    path('posts/<int:pk>/like', PostLikeCreate.as_view()),
    path('comments', CommentList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
    path('posts/<int:pk>/comments', PostCommentList.as_view()),
    path('signup', UserCreate.as_view())
]
