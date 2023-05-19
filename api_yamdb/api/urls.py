from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, GenreViewSet, TitleViewSet

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('title', TitleViewSet, basename='title')
router_v1.register('genre', GenreViewSet, basename='genre')
