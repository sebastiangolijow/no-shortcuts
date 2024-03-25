from django.urls import path
from .views import ResponseListCreate, ResponseUpdateDeleteView

urlpatterns = [
    path(
        "article/<uuid:article_id>/",
        ResponseListCreate.as_view(),
        name="response-create",
    ),
    path(
        "<uuid:id>/",
        ResponseUpdateDeleteView.as_view(),
        name="response-delete-update",
    ),
]
