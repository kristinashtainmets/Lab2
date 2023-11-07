from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


from .models import CustomUser
from .models import Application


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

class ChangeRequestStatusForm(forms.ModelForm):
    comment = forms.CharField(required=False)
    design = forms.ImageField(required=False)

    class Meta:
        model = Application
        fields = ['status', 'comment', 'design']

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        comment = cleaned_data.get('comment')
        design = cleaned_data.get('design')

        if status == Application.P and not comment:
            self.add_error('comment', 'Комментарий обязателен при смене статуса на "Принято в работу".')
        elif status == Application.C and not design:
            self.add_error('design', 'Дизайн обязателен при смене статуса на "Выполнено".')
