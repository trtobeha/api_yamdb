from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import User


# сериализатор токена
class TokenSerializer(TokenObtainPairSerializer):
    confirmation_code = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = '__all__'


# сериализатор юзера
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


# сериализатор регистрации
class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+\Z',
        max_length=150,
        required=True,
    )
    email = serializers.EmailField(
        max_length=254,
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" недоступно.'
            )
        if User.objects.filter(
            email=data['email'], username=data['username']
        ).exists():
            return data
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('Этот email уже занят.')
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError('Это имя уже занято.')
        return data
