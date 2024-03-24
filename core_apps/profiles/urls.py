from django.urls import path
from .views import (
    ProfileListAPIView,
    ProfileDetailAPIView,
    UpdatePRofileAPIView,
    FollowerListView,
    FollowAPIView,
    UnfollowAPIView,
)

urlpatterns = [
    path("all/", ProfileListAPIView.as_view(), name="all-profiles"),
    path("me/", ProfileDetailAPIView.as_view(), name="detail-profile"),
    path("me/update/", UpdatePRofileAPIView.as_view(), name="update-profile"),
    path("me/followers/", FollowerListView.as_view(), name="followers"),
    path("<uuid:user_id>/follow", FollowAPIView.as_view(), name="follow"),
    path("<uuid:user_id>/unfollow", UnfollowAPIView.as_view(), name="unfollow"),
]
