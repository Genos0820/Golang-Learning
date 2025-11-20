from django.urls import path
from . import views

urlpatterns=[
    path('',views.ReviewView.as_view()),
    path('thankyou',views.ThankyouView.as_view()),
    path('feedbacks',views.FeedbacksView.as_view()),
    path('feedbacks/favorite',views.AddFavouriteView.as_view()),
    path('review_detail/<int:pk>',views.ReviewDetailView.as_view(),name='review_detail'),
]