from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username