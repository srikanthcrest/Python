from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import BasePermission,AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import CustomUser
from rest_framework.exceptions import PermissionDenied

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class IsAdminUserType(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False
        
        # Check if the user is an admin (user_type = 1)
        if request.user.user_type != '1':
            # If not an admin, raise a custom PermissionDenied exception
            raise PermissionDenied(detail="You must be an admin to access this resource.")
        
        return True

class ListUsers(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserType]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)