from django import forms
from . models import Task,Search
from django.forms.widgets import DateInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter old password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}))
class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already registered.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username


class TaskForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),  # All users will appear in the dropdown
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model=Task
        fields= [
            'name',
            'user',
            'status',
            'deadline',
            'description'
        ]
        widgets = {
            'deadline': DateInput(attrs={'type': 'date'}),
        }

class SearchForm(forms.ModelForm):
    class Meta:
        model=Search
        fields=['search']