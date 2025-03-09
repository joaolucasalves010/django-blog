from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class CustomRegisterForm(UserCreationForm):
  
  username = forms.CharField(
    label="Username",
    widget=forms.TextInput(attrs={
      "class": "form-control",
      "placeholder": "Digite seu usuário"
    })
  )
  
  password1 = forms.CharField(
    label="Senha",
    widget=forms.PasswordInput(attrs={
      "class": "form-control",
      "placeholder": "Digite sua senha"
    })
  )
  
  password2 = forms.CharField(
    label="Confirme sua senha",
    widget=forms.PasswordInput(attrs={
      "class": "form-control",
      "placeholder": "Confirme sua senha"
    })
  )
  
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']


class CustomLoginForm(AuthenticationForm):
  
  username = forms.CharField(
    label="Usuário",
    widget=forms.TextInput(attrs={
      "class": "form-control",
      "placeholder": "Digite seu usuário"
    })
  )

  password = forms.CharField(
    label="Senha",
    widget=forms.PasswordInput(attrs={
      "class": "form-control",
      "placeholder": "Digite sua senha"
    })
  )

