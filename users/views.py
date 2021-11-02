from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from users.models import CustomUser
from users.permissions import UserAccessOrReadOnly
from users.serializers import (
    UserListSerializer, UserCreateSerializer, UserDetailSerializer,
)


class UserListViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'create':
            return UserCreateSerializer


class UserDetailView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [UserAccessOrReadOnly]
    http_method_names = ['get', 'put', 'head']