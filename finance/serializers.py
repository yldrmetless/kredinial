from rest_framework import serializers
from .models import Bank, InterestRate

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'name', 'ihtiyac_url', 'konut_url', 'tasit_url', 'kobi_url', 'image']  # Yeni alanlar eklendi

class InterestRateSerializer(serializers.ModelSerializer):
    bank = BankSerializer() 
    
    class Meta:
        model = InterestRate
        fields = ['id', 'bank', 'term', 'rate', 'annual_cost_rate', 'loan_type']
