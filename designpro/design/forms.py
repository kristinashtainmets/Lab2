from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


from .models import CustomUser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        full_name = cleaned_data.get('full_name')
        if not all(x.isalpha() or x.isspace() for x in full_name):
            raise ValidationError('ФИО может содержать только буквы и пробелы.')


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "full_name", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.full_name = self.cleaned_data["full_name"]
        if commit:
            user.save()
        return user

