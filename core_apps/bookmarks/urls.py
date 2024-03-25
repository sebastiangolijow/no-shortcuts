from django.urls import path
from .views import BookMarkCreateView, BookmarkDestroyView

urlpatterns = [
    path(
        "bookmark_article/<uuid:article_id>/",
        BookMarkCreateView.as_view(),
        name="bookmark-create-article",
    ),
    path(
        "remove_bookmark/<uuid:article_id>/",
        BookmarkDestroyView.as_view(),
        name="bookmark-destroy-article",
    ),
]
