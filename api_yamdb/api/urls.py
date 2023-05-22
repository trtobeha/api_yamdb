from rest_framework.routers import DefaultRouter

from django.urls import include, path

from api.views import CategoryViewSet, GenreViewSet, TitleViewSet

router_v1 = DefaultRouter()
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('title', TitleViewSet, basename='title')
router_v1.register('genre', GenreViewSet, basename='genre')
urlpatterns = [
    # api/v1/auth/signup - ссылка для post-запроса на регистрацию
]
