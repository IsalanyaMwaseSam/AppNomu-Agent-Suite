from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractBaseUser
from .models import *
from django.core.exceptions import ValidationError


class RegForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your name', 'id':'email', 'name':'email'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your District, Subcounty, Village' ,'id':"location"}))
    nin = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your NIN', 'id':"NIN",'name':"nin"}))
    LC1_letter = forms.FileField(widget=forms.FileInput(attrs={'name':'upload'}))
    National_Id = forms.FileField(widget=forms.FileInput(attrs={'name':'upload'}))

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)

        for fieldname in ['LC1_letter', 'nin','password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = Account
        fields = ['email', 'name', 'address', 'phone_number', 'LC1_letter', 'nin', 'National_Id', 'password1', 'password2']

        