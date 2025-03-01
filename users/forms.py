from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.template.defaultfilters import first
from django.core.exceptions import ValidationError


from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'username': 'Имя пользователя:',
            'email': 'Email:',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'password1': 'Пароль:',
            'password2': 'Подтверждение пароля:',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Этот никнейм уже занят.")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 4 or len(password1) > 16:
            raise ValidationError("Пароль должен содержать от 4 до 16 символов")
        if '*' in password1 or '&' in password1 or '{' in password1 or '}' in password1 or '|' in password1 or '+' in password1:
            raise ValidationError("Не должно быть символов из набора: * & { } | +")
        if not any(char.isupper() for char in password1):
            raise ValidationError("Пароль должен содержать хотя бы одну заглавную букву")
        if not any(char.isdigit() for char in password1):
            raise ValidationError("Пароль должен содержать хотя бы одну цифру")
        return password1

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Имя пользователя:',
            'email': 'Email:',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''
