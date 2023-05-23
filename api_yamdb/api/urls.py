from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (UserViewSet, CategoryViewSet, GenreViewSet,
                    TitleViewSet, ReviewViewSet, CommentViewSet,
                    TokenViewSet, SignUpViewSet,)

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('categories', CategoryViewSet, basename='categories')
router.register('titles', TitleViewSet, basename='titles')
router.register('genres', GenreViewSet, basename='genres')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(router.urls)),
    # path('auth/signup/', SignUpViewSet.as_view(), name='signup'),
    # path('auth/token/', TokenViewSet.as_view(), name='get_token'),
]
