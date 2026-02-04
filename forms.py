from django import forms
from .models import Medicine
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'stock']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
