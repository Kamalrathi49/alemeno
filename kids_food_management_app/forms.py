from dataclasses import field
from django import forms
from kids_food_management_app.models import *
from kids_food_management_app.utils.choices import *


class addKidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = "__all__"

class addFoodForm(forms.ModelForm):
    is_approved = forms.ChoiceField(choices=APPROVE_CHOICES, widget=forms.RadioSelect(attrs={
        'class': 'form-control',
        'style': 'cursor: pointer; margin-bottom: 20px;',
        }), label='Is Approved')
    food_group = forms.ChoiceField(choices=FOOD_GROUP_CHOICES, widget=forms.RadioSelect(attrs={
        'class': 'form-control mb-4',
        'style': 'cursor: pointer; margin-bottom: 20px;',
        }), label='Select Group')

    class Meta:
        model = Food
        fields = ('image', 'food_group', 'is_approved', 'approved_by')