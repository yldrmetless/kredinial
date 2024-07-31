from django.db import models
from cloudinary.models import CloudinaryField

class Bank(models.Model):
    name = models.CharField(max_length=100, unique=True)
    ihtiyac_url = models.URLField(max_length=200, blank=True, null=True)  # 
    konut_url = models.URLField(max_length=200, blank=True, null=True)  # 
    tasit_url = models.URLField(max_length=200, blank=True, null=True)  # 
    kobi_url = models.URLField(max_length=200, blank=True, null=True)  # 
    image = CloudinaryField('image', blank=True, null=True) 

    def __str__(self):
        return self.name

class InterestRate(models.Model):
    LOAN_TYPE_CHOICES = [
        ('İhtiyaç Kredisi', 'İhtiyaç Kredisi'),
        ('Konut Kredisi', 'Konut Kredisi'),
        ('Taşıt Kredisi', 'Taşıt Kredisi'),
        ('Kobi Kredisi', 'Kobi Kredisi'),
    ]

    TERM_CHOICES = [
        ('3 ay', '3 ay'),
        ('6 ay', '6 ay'),
        ('9 ay', '9 ay'),
        ('12 ay', '12 ay'),
        ('18 ay', '18 ay'),
        ('24 ay', '24 ay'),
        ('30 ay', '30 ay'),
        ('36 ay', '36 ay'),
    ]

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    term = models.CharField(max_length=10, choices=TERM_CHOICES)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    annual_cost_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPE_CHOICES)

    class Meta:
        unique_together = ('bank', 'term', 'loan_type')

    def __str__(self):
        return f"{self.bank.name} - {self.term} Ay - {self.loan_type} - Faiz: {self.rate}% - Yıllık Maliyet: {self.annual_cost_rate}%"
