from rest_framework import viewsets

from django.db.models import Avg
from django.shortcuts import get_object_or_404

from reviews.models import Category, Comment, Genre, Review, Title, User

from .serializers import CommentSerializer, ReviewSerializer


class ReviewVieWSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    # permission_classes =

    def get_queryset(self):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
        serializer.save(author=self.request.user, title=title)


class CommentVieWSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # permission_classes =

    def get_queryset(self):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id')
        )
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            id=self.kwargs.get('review_id')
        )
        serializer.save(author=self.request.user, review=review)

# добавить в TitleViewSet:

# queryset = Title.objects.annotate(
#        rating=Avg('reviews__score')
#    ).all()
