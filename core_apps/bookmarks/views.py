from rest_framework import generics, permissions
from .models import Bookmark
from .serializers import BookmarkSerializer
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError, NotFound
from core_apps.articles.models import Article
from uuid import UUID


class BookMarkCreateView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        article_id = self.kwargs.get("article_id")
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
            except Article.DoesNotExist:
                raise ValidationError("Invalid ID")
        else:
            raise ValidationError("article id required")

        try:
            serializer.save(user=self.request.user, article=article)
        except IntegrityError:
            raise ValidationError("you have already bookmarked this article")


class BookmarkDestroyView(generics.DestroyAPIView):
    queryset = Bookmark.objects.all()
    lookup_field = "article_id"
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        article_id = self.kwargs.get("article_id")
        try:
            UUID(str(article_id), version=4)

        except ValueError:
            raise ValidationError("invalid article id provided")

        try:
            bookmark = Bookmark.objects.get(user=user, article__id=article_id)
        except Bookmark.DoesNotExist:
            raise NotFound("bookmark not found")
        return bookmark

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.user != user:
            raise ValidationError("ypu cant delete a bookmark that is not yours")
        instance.delete()
