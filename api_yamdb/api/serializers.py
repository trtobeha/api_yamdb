from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title, User
from django.shortcuts import get_object_or_404


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )

    class Meta:
        model = Title
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    def validate(self, attrs):
        request = self.context['request']
        title = get_object_or_404(Title)  # id=)
        if request.method == 'POST':
            if Review.objects.filter(
                title=title,
                author=request.user
            ).exists():
                raise serializers.ValidationError(
                    'Вы можете оставить только один отзыв'
                )
        return attrs

    def validate_score(self, value):
        if 0 > value > 10:
            raise serializers.ValidationError('Оценка от 0 до 10')
        return value

    class Meta:
        fields = ()
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        read_only=True,
        slug_field='text',
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment
