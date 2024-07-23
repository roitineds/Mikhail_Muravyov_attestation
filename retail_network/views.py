from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Network
from .permissions import IsActiveEmployee
from .serializers import NetworkSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class NetworkViewSet(viewsets.ModelViewSet):
    """
    Набор представлений CRUD для модели поставщика.
    """
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    filter_backends = [SearchFilter]
    search_fields = ['country']
    permission_classes = [IsActiveEmployee]


class MyTokenObtainPairView(TokenObtainPairView):
    pass


class MyTokenRefreshView(TokenRefreshView):
    pass

