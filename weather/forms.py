from django.forms import ModelForm, fields, widgets
from .models import(
    City
)

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': widgets.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'City Name'
            }
        )}