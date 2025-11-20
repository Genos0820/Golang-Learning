from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.Fp.as_view(),name="starting-page"),
    path('posts',views.Posts.as_view(),name="posts-page"),
    path('posts/<slug:slug>',views.PostDetail.as_view(),name="post-detail-page"), # /posts/my-first-post
    path('read-later',views.ReadLaterView.as_view(),name="read-later"),
]
