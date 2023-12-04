from django import forms
from work.models import Books


class EmpForm(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.CharField()
    contact=forms.CharField()


class BookForm(forms.Form):
    title=forms.CharField()
    author=forms.CharField()
    publicationyear=forms.CharField()
    genre=forms.CharField()


class BooksForm(forms.ModelForm):
    class Meta:
        model=Books
        fields='__all__'  




