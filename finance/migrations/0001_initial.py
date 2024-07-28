# Generated by Django 5.0.7 on 2024-07-26 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterestRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(choices=[('3 ay', '3 ay'), ('6 ay', '6 ay'), ('9 ay', '9 ay'), ('12 ay', '12 ay'), ('18 ay', '18 ay'), ('24 ay', '24 ay'), ('30 ay', '30 ay'), ('36 ay', '36 ay')], max_length=10)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('annual_cost_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('loan_type', models.CharField(choices=[('İhtiyaç Kredisi', 'İhtiyaç Kredisi'), ('Konut Kredisi', 'Konut Kredisi'), ('Taşıt Kredisi', 'Taşıt Kredisi'), ('Kobi Kredisi', 'Kobi Kredisi')], max_length=20)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.bank')),
            ],
            options={
                'unique_together': {('bank', 'term', 'loan_type')},
            },
        ),
    ]
