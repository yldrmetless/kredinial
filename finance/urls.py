from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BankViewSet, InterestRateViewSet

router = DefaultRouter()
router.register(r'banks', BankViewSet)
router.register(r'interest-rates', InterestRateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
