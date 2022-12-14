from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=1000) # mysql varchar 주의
    email = models.EmailField(max_length=50, null=True)
    phoneNumber = PhoneNumberField(unique = True, null = True, blank = False)
    connect = models.TextField(null=True)
    family = models.TextField(null=True)
    kind = models.BooleanField(null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []