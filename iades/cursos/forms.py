from django import forms


class InstructorForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    especialidad = forms.CharField(max_length=100)