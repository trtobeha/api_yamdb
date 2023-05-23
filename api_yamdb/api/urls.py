from rest_framework.routers import DefaultRouter

from django.urls import include, path

from api.views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    SignUpViewSet,
    TitleViewSet,
    TokenViewSet,
    UserViewSet,
)

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')
router.register('genres', GenreViewSet, basename='genres')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews',
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignUpViewSet.as_view({'get': 'list'}), name='signup'),
    path('v1/auth/token/', TokenViewSet.as_view({'get': 'list'}), name='get_token'),
]
