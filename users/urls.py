from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from users import views

app_name = 'users'

router = routers.DefaultRouter()
router.register('users', views.UserListViewSet)

urlpatterns = [
    path(
        '<int:pk>/',
        views.UserDetailView.as_view({'get': 'retrieve', 'put': 'update'}),
        name='detail'
    ),
    path('login/', jwt_views.TokenObtainPairView().as_view(), name='login'),
    path('login/refresh/', jwt_views.TokenRefreshView().as_view(),
         name='token-refresh'),
]
