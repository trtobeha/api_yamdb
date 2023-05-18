from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from rest_framework import filters, viewsets

from reviews.models import Category, Genre, Title
from .mixins import ListCreateViewSet
from .permissions import (IsAdminOrReadOnly)
from .serializers import (CategorySerializer,
                          GenreSerializer,
                          TitleSerializer)


class CategoryViewSet(ListCreateViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(ListCreateViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
