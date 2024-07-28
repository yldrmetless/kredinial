from django.contrib import admin
from .models import Bank, InterestRate

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'ihtiyac_url', 'konut_url', 'tasit_url', 'kobi_url', 'image')  # Yeni alanlar eklendi

@admin.register(InterestRate)
class InterestRateAdmin(admin.ModelAdmin):
    list_display = ('bank', 'term', 'loan_type', 'rate', 'annual_cost_rate')
    list_filter = ('bank', 'term', 'loan_type')
    search_fields = ('bank__name', 'loan_type')
