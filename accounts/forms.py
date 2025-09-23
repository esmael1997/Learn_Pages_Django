from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()



class SignUpForm(UserCreationForm):
    class Meta:
        model = User             
        fields = ("username", "email", "password1", "password2")



class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")



class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "password1", "password2")  


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")  
