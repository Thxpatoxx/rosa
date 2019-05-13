from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Implementodep, Factura

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    fecha_de_nacimiento = forms.DateField(required=True)
    numero_de_telefono = forms.IntegerField(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'fecha_de_nacimiento',
            'numero_de_telefono',
            'password1',
            'password2',
        )
    def save(self,commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.fecha_de_nacimiento = self.cleaned_data['fecha_de_nacimiento']
        user.numero_de_telefono = self.cleaned_data['numero_de_telefono']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ImplementodepForm(forms.ModelForm):
    class Meta:
        model = Implementodep
        fields = ()

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('horas','pago')