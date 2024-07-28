# Generated by Django 5.0.7 on 2024-07-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bank_images/'),
        ),
        migrations.AddField(
            model_name='bank',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
