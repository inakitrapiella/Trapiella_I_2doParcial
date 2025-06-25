from django import forms


class consultasForm(forms.Form):
    nombre = forms.CharField(max_length=255, label= 'nombre')
    email = forms.EmailField(max_length=255, label= 'email')
    mensaje = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electronico')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

class RegistroForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
