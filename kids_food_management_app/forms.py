from dataclasses import field
from django import forms
from kids_food_management_app.models import *
from kids_food_management_app.utils.choices import *


class addKidForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'style':'margin-bottom: 20px;',
        'required': 'required',}))
    age = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'style':'margin-bottom: 20px;',
        'required': 'required',}))
    # parents_phone_number = forms.CharField(widget=forms.NumberInput(attrs={
    #     'class': 'form-control',
    #     'style':'margin-bottom: 20px;',
    #     'placeholder' : "Enter parents's phone no.",
    #     'required': 'required',}))
    parents_email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'style':'margin-bottom: 20px;',
        'required': 'required',}))
    class Meta:
        model = Kid
        fields = "__all__"

class addFoodForm(forms.ModelForm):

    image = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : 'Enter Food image link',
        'id': 'source',
        'required': 'required',}))
    is_approved = forms.ChoiceField(choices=APPROVE_CHOICES, widget=forms.RadioSelect(attrs={
        'class': 'form-control',
        'style': 'cursor: pointer; margin-bottom: 20px;',
        'required': 'required',
        }), label='Is Approved')
    approved_by = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder' : "Enter approver's name",
        'required': 'required',}))
    food_group = forms.ChoiceField(choices=FOOD_GROUP_CHOICES, widget=forms.RadioSelect(attrs={
        'class': 'form-control mb-4',
        'style': 'cursor: pointer; margin-bottom: 20px;',
        'required': 'required',
        }), label='Select Group')

    class Meta:
        model = Food
        fields = ('image', 'food_group', 'is_approved', 'approved_by')