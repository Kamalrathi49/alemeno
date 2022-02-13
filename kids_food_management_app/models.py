from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from kids_food_management_app.utils.choices import *

class Kid(models.Model):
    name = models.CharField(max_length=99)
    age = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    parents_phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True) 
    parents_email = models.EmailField()

    def __str__(self) -> str:
        return self.name

class Food(models.Model):
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999)
    food_group = models.CharField(choices=FOOD_GROUP_CHOICES, max_length=15)
    is_approved = models.CharField(choices=APPROVE_CHOICES, max_length=5, blank=True)
    approved_by = models.CharField(max_length=299)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    updated_on = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f"{self.kid} {self.approved_by}"
