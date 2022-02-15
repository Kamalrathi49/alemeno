from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from kids_food_management_app.utils.choices import *

class Kid(models.Model):
    name = models.CharField(max_length=99, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    parents_email = models.EmailField(blank=True, null=True)
    parents_phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True) 

    def __str__(self) -> str:
        return self.name

class Food(models.Model):
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE, blank=True, null=True)
    image = models.CharField(max_length=9999, blank=True, null=True)
    food_group = models.CharField(choices=FOOD_GROUP_CHOICES, max_length=15, blank=True, null=True)
    is_approved = models.CharField(choices=APPROVE_CHOICES, max_length=5, blank=True, null=True)
    approved_by = models.CharField(max_length=299, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.kid} {self.approved_by}"
