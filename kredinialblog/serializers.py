from rest_framework import serializers
from .models import BlogPost, Comment, Category
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class BlogPostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author_full_name", read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "content",
            "cover_image",
            "created_at",
            "updated_at",
            "author",
            "slug",
            "categories",
            "author_name",
        ]


# serializers.py
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')  # Mevcut alanlar
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_first_name', 'author_last_name', 'content', 'created_at']
        read_only_fields = ['author', 'author_first_name', 'author_last_name', 'created_at', 'post']
