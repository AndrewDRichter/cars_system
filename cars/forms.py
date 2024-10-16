from django import forms
from .models import Brand, Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data.get('value')
        print(value)
        if value < 20000:
            self.add_error('value', 'Valor mínimo deve ser de 20.000')
        return value