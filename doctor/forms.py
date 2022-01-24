from django import forms
from .models import Doctor
class UserForm(forms.ModelForm):
    class Meta:
        model = Doctor
        widgets = {
        'password': forms.PasswordInput(),
        }
   