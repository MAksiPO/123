from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import TextInput

from .models import CustomUser, TodoItem
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(
        attrs={'class': 'form-field', 'placeholder': "Имя"}
    ))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
        attrs={'class': 'form-field', 'placeholder': "Фамилия"}
    ))
    email = forms.CharField(label="Почта", widget=forms.EmailInput(
        attrs={'class': 'form-field','type': "text", 'placeholder': "Почта"}
    ))
    phone = forms.CharField(label="Телефон", widget=forms.TextInput(
        attrs={'class': 'form-field', 'placeholder': "Телефон"}
    ))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-field', 'placeholder': "Пароль"}))
    password2 = forms.CharField(label='Подтверждение Пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-field', 'placeholder': "Подтверждение Пароля"}))

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name', 'username', 'email', 'phone', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.TextInput(attrs={'class': 'form-field', 'placeholder': "Имя пользователя"})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-field',
                                                                 'placeholder': "Пароль"}))
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class TodoForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = ['reminder_type', 'task_name', 'description',
                  'status', 'notification_method', 'scores', 'subscribers']

        widgets = {
            'task_name': TextInput(attrs={
                'class': 'field has-addons',
                'placeholder': 'имя задачи'
            }),
        }