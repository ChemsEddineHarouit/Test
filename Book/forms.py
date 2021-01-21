from django import forms
from .models import BookModel as Book


class BookForm(forms.ModelForm):
    class Meta:
        model   = Book
        fields = ['title', 'cover']