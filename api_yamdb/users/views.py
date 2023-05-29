from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import get_object_or_404

from users.models import User
from users.permissions import IsAdmin
from users.serializers import (GetTokenSerializer, SignUpSerializer,
                               UserSerializer)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_token(request):
    serializer = GetTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username'],
    )
    if default_token_generator.check_token(
        user,
        serializer.validated_data['confirmation_code'],
    ):
        token = AccessToken.for_user(user)
        return Response({'token': str(token)}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ('username',)
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'username'
    permission_classes = [IsAdmin]
    http_method_names = [
        'get',
        'post',
        'patch',
        'delete',
    ]

    @action(
        methods=('get', 'patch'),
        url_path='me',
        detail=False,
        serializer_class=UserSerializer,
        permission_classes=(permissions.IsAuthenticated,),
    )
    def me(self, request):
        if request.method == 'GET':
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        serializer = UserSerializer(
            request.user,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(role=request.user.role)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def signup(request):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data['username']
    email = serializer.validated_data['email']

    if User.objects.filter(Q(username=username) | Q(email=email)).exists():
        return Response(
            serializer.errors,
            status=status.HTTP_200_OK,
        )
    else:
        user, created = User.objects.get_or_create(
            username=username,
            email=email,
        )
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            'Код подтверждения для завершения регистрации:',
            confirmation_code,
            'ya@mdb.com',
            [email],
            fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
