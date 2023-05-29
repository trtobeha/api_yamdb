from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from django.db.models import Avg

from titles.filters import TitlesFilter
from titles.mixins import ListCreateViewSet
from titles.models import Category, Genre, Title
from titles.serializers import (CategorySerializer, GenreSerializer,
                                TitleReadSerializer, TitleWriteSerializer)
from users.permissions import IsAdminOrReadOnly


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
    queryset = Title.objects.annotate(rating=Avg('reviews__score')).all()
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitlesFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer
