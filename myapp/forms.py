from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"

class PackageForm(forms.ModelForm):
    class Meta:
        model=Package_Master
        fields="__all__"

class Booking_packageForm(forms.ModelForm):
    class Meta:
        model=Booking_Package
        fields="__all__"