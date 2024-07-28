from rest_framework import viewsets
from .models import Bank, InterestRate
from .serializers import BankSerializer, InterestRateSerializer

class BankViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class InterestRateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InterestRate.objects.all()
    serializer_class = InterestRateSerializer
