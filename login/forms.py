from django import forms


class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
        label='Usuário', error_messages={'invalid': 'Usuário deve conter apenas letras e números'})

    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
        label='Email',error_messages={'invalid': 'E-mail inválido'})

    password = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, render_value=False)), label='Senha')

    password2 = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30, render_value=False)), label='Confirme sua senha')