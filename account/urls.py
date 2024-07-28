from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminProfileViewSet, UserCreateView, UserLoginView, get_user, UpdateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'admin_profiles', AdminProfileViewSet)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('user/', get_user, name='user-detail'),  # Yeni eklenen endpoint
    path('user/update/', UpdateUserView.as_view(), name='update_user'),  # Kullanıcı güncelleme için endpoint
    path('', include(router.urls)),  # Admin profile URLs
]
