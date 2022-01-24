from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.forms import fields
from django.forms.utils import ValidationError
from django import forms

from .models import CustomUser

class CustomeUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomeUserCreationForm, self).__init__(*args, **kwargs)
        del self.fields['username']
    
    class Meta:
        model = CustomUser
        fields = ("email",)

class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email','password1','password2','first_name','last_name', 'phone','province','regencies')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2 :
            raise forms.ValidationError("Password doesn't match")
        return password2

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        user.username = user.email

        if commit :
            user.save()
        return user

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email','first_name','last_name','username')