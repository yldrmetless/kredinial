# Generated by Django 5.0.7 on 2024-07-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminprofile',
            name='cv',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
