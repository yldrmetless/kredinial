from django.db import models
from django.contrib.auth.models import User

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    cv = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
