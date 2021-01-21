from django import forms
from .models import AuthorModel as Author

class DateInput(forms.DateInput):
    input_type='date'

class AuthorForm(forms.ModelForm):
    class Meta:
        model   = Author
        fields = '__all__'
        widgets = {
            'birth_date' : DateInput(format='%Y-%m-%d'),
        }