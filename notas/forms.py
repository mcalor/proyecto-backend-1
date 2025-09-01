from django import forms
from .models import Nota


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['titulo', 'contenido']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'formcontrol', 'placeholder': 'Título'}),
            'contenido': forms.Textarea(attrs={'class': 'formcontrol', 'rows': 6, 'placeholder': 'Escribe tu nota...'}),
            }
    def clean_titulo(self):
        titulo = self.cleaned_data['titulo'].strip()
        if len(titulo) < 3:
            raise forms.ValidationError("El título debe tener al menos 3 caracteres.")
        return titulo