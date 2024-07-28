from rest_framework import viewsets
from rest_framework import status, views
from .models import AdminProfile
from .serializers import AdminProfileSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserUpdateSerializer


class AdminProfileViewSet(viewsets.ModelViewSet):
    queryset = AdminProfile.objects.all()
    serializer_class = AdminProfileSerializer


class UserCreateView(views.APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'detail': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)



class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        # Mevcut şifreyi doğrula
        current_password = data.get('current_password')
        if not user.check_password(current_password):
            return Response({"detail": "Mevcut şifre yanlış."}, status=status.HTTP_400_BAD_REQUEST)

        # Kullanıcı bilgilerini güncelle
        user.email = data.get('email', user.email)
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)

        new_password = data.get('new_password')
        if new_password:
            user.set_password(new_password)

        user.save()
        return Response({
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }, status=status.HTTP_200_OK)