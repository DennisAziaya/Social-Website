from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    user_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
