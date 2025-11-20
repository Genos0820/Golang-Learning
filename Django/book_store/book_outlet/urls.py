from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name="all-books"),
    path('book_detail/<slug:slug>',views.bookDetails,name="book-detail-page"),
]
