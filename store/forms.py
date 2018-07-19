from django import forms
from django.contrib.auth import authenticate
from .models import *
from datetime import datetime
from dateutil.relativedelta import relativedelta


class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"placeholder": "Имя пользователя",
                                                                            "class": "form-control"}))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={"placeholder": "Пароль",
                                                                                "class": "form-control"}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Неправильный логин/пароль")


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"placeholder": "Имя пользователя",
                                                                            "class": "form-control"}))
    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={"placeholder": "Пароль",
                                                                                "class": "form-control"}))
    confirm_password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={"placeholder": "Повтор пароля",
                                                                                        "class": "form-control"}))
    email = forms.CharField(max_length=32, widget=forms.EmailInput(attrs={"placeholder": "E-mail",
                                                                          "class": "form-control"}))
    first_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"placeholder": "Имя",
                                                                              "class": "form-control"}))
    last_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"placeholder": "Фамилия",
                                                                             "class": "form-control"}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"placeholder": "Дата рождения",
                                                                  "class": "form-control",
                                                                  "type": "date",
                                                                  "value": datetime.now().date()}))
    # code_from_email = forms.CharField(required=False, max_length=6, min_length=6, widget=forms.TextInput(
    #     attrs={"placeholder": "Код из письма", "class": "form-control"}))

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        date_of_birth = cleaned_data.get("date_of_birth")
        user = None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            pass
        if user is not None:
            raise forms.ValidationError("Пользователь с таким логином уже зарегистрирован")
        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")
        if relativedelta(datetime.now().date(), date_of_birth).years < 18:
            raise forms.ValidationError("Ты еще слишком мал")


class UserForm(forms.Form):
    username = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"placeholder": "Имя пользователя",
                                                                            "class": "form-control"}))
    email = forms.CharField(max_length=32, widget=forms.EmailInput(attrs={"placeholder": "E-mail",
                                                                          "class": "form-control"}))
    first_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"placeholder": "Имя",
                                                                              "class": "form-control"}))
    last_name = forms.CharField(max_length=16, widget=forms.TextInput(attrs={"placeholder": "Фамилия",
                                                                             "class": "form-control"}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"placeholder": "Дата рождения",
                                                                  "class": "form-control"}))


class ResetPasswordForm(forms.Form):
    pass
