from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
from .models import Issue
from django import forms

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['student_name', 'book', 'no_of_days']
