from django import forms
from django.forms import TextInput, Textarea

from . models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ["title", "author", "description", "pub_year"]
        widgets = {
            'title': TextInput(attrs:={
                'class': "book-title",
                'style': 'margin-left: 50px; margin-bottom: 10px; width: 315px',
            }),
            'author': TextInput(attrs:={
                'class': "book-author",
                'style': 'margin-left: 70px; margin-bottom: 10px; width: 315px',
            }),
            'description': Textarea(attrs:={
                'class': "book-description",
                'style': 'margin-bottom: 2px',
            }),
            'pub_year': TextInput(attrs:={
                'class': "book-year",
                'style': 'margin-left: 10px; margin-top: 10px; width: 315px',
            })
        }
