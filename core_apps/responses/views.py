from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from .models import Article, Responses
from .serializers import ResponseSerializer
from rest_framework.exceptions import PermissionDenied


class ResponseListCreate(generics.ListCreateAPIView):
    queryset = Responses.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResponseSerializer

    def get_queryset(self):
        article_id = self.kwargs.get("article_id")
        return Responses.objects.filter(article__id=article_id, parent_response=None)

    def perform_create(self, serializer):
        user = self.request.user
        article_id = self.kwargs.get("article_id")
        article = get_object_or_404(Article, id=article_id)
        serializer.save(user=user, article=article)


class ResponseUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Responses.objects.all()
    lookup_field = "id"
    serializer_class = ResponseSerializer

    def perform_update(self, serializer):
        user = self.request.user
        response = self.get_object()
        if user != response.user:
            raise PermissionDenied("ypu dont have permission here")
        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        response = self.get_object()
        if user != response.user:
            raise PermissionDenied("ypu dont have permission here")
        instance.delete()
