from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, CommentViewSet,CategoryViewSet

router = DefaultRouter()
router.register(r'blogs', BlogPostViewSet, basename='blog')
router.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = [
    path('posts/<slug:post_slug>/comments/', CommentViewSet.as_view({'post': 'create', 'get': 'list'}), name='comment-list-create'),
    path('posts/<slug:post_slug>/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment-detail'),
] + router.urls