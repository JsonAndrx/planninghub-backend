#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#Utilities
from apps.utils.models import PlanningModel


class User(PlanningModel, AbstractUser):
    
    email = models.EmailField(unique=True, error_messages={'unique':'A user with email already exists.'})
    phone_regex = RegexValidator(regex=r'\+?1?\d{10}$', message='Phone number must be entered in the format: +5555555555')
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]
    is_client = models.BooleanField('client', default=True)
    is_verified = models.BooleanField('verified', default=True)

    def __str__(self):
        return self.username
    
