from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    username = forms.CharField(
                            label='Username',
                            max_length=100,
                            min_length=5,
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(
                            label='Password',
                            max_length=100,
                            min_length=5,
                            widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(
                            label='Confirm Pasword',
                            max_length=100,
                            min_length=5,
                            widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('Emails is already registered')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError('Username is already registered')
        return username

    # def clean_password1(self):
    #     this will raise a key error because it refences password2
    #     which is ran after password1 validation
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 != p2:
    #         raise ValidationError('Passwords does not match')
    #     return p1


    # def clean_password2(self):
    #     p1 = self.cleaned_data['password1']
    #     p2 = self.cleaned_data['password2']
    #     if p1 != p2:
    #         raise ValidationError('Passwords does not match')
    #     return p2


    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')

        if p1 and p2:
            if p1 != p2:
                raise ValidationError('Passwords does not match')
