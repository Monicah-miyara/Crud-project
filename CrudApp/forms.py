from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields=['fullname','age','course']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","last_name","password1","password2"]
        widgets = {
            'fullname':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'course':forms.TextInput(attrs={'class':'form-control'}),
        }