from django import forms
from .models import Contacto , Producto
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class ContactoForm(forms.ModelForm):

    # nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Contacto
        fields = '__all__'

       

class ProductoForm(forms.ModelForm):
    imagen = forms.ImageField(required=False , validators=[MaxSizeFileValidator(max_file_size=2)] )
    nombre = forms.CharField(max_length=50 ,min_length=3)
    precio = forms.IntegerField(min_value=1 , max_value=1500000)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()
        if existe:
            raise forms.ValidationError("Este nombre ya existe")
        return nombre



    class Meta:
        model = Producto
        fields = '__all__'
        
        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }

class CustomUserCreationform(UserCreationForm):



   class Meta:
    model = User
    fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
