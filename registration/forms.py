from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 caracteres como máximo y debe ser valido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    #* en la nueva version de django ya no es necesario este metodo
    # def clean_email(self):
    #     # recupera el email al enviar el formulario
    #     email = self.cleaned_data.get["email"]
    #     # valida si el email ya existe en la base de datos
    #     if User.objects.filter(email=email).exists():
    #         # si el email ya existe, lanza un error de validacion
    #         raise forms.ValidationError("El email ya existe")
    #     return email