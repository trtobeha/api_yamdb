from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.shortcuts import get_object_or_404

from reviews.models import Comment, Review
from titles.models import Title


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = '__all__'
        model = Review

    def validate_score(self, value):
        if 0 > value > 10:
            raise serializers.ValidationError('Оценка от 0 до 10')
        return value

    def validate(self, data):
        request = self.context['request']
        author = request.user
        title_id = self.context.get('view').kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        if (
            request.method == 'POST'
            and Review.objects.filter(title=title, author=author).exists()
        ):
            raise ValidationError(
                'Вы не можете добавить более ' 'одного отзыва на произведение',
            )
        return data


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
        fields = '__all__'
        model = Comment
