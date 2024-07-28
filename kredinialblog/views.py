from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from .models import BlogPost, Comment, Category
from .serializers import BlogPostSerializer, CommentSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

# views.py
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['create']:
            return [IsAuthenticated()]  # Yalnızca giriş yapan kullanıcılar yorum yapabilir
        return []

    def perform_create(self, serializer):
        post_slug = self.kwargs.get('post_slug')
        if not post_slug:
            raise NotFound("Post slug not found.")
        post = get_object_or_404(BlogPost, slug=post_slug)
        serializer.save(
            author=self.request.user, 
            post=post,
            author_first_name=self.request.user.first_name,
            author_last_name=self.request.user.last_name
        )

    def get_queryset(self):
        post_slug = self.kwargs.get('post_slug')
        if post_slug:
            return Comment.objects.filter(post__slug=post_slug)
        return Comment.objects.all()
    
    
    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.author != request.user:
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)






class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            return BlogPost.objects.all()
        return BlogPost.objects.all()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated and self.request.user.is_staff:
            serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAuthenticated()]
        return []
