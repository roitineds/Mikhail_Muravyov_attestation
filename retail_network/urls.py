from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import RetailNetworkConfig
from .views import NetworkViewSet, MyTokenObtainPairView, MyTokenRefreshView

router = DefaultRouter()
router.register(r'networks', NetworkViewSet, basename='network')

app_name = RetailNetworkConfig.name

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]
