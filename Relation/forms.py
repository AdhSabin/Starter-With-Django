from django import forms
from . models import Publisher,Author,Book

class PublisherForm(forms.ModelForm):
    class Meta:
        model=Publisher
        fields = ['name','address','city','country']
        widgets = {
            'address':forms.Textarea(attrs={'row':3})
        }
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name','last_name','email']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','isbn','published_date','publisher','authors','image']
        widgets = {
            'published_date':forms.DateInput(attrs={'type':'date'}),
            'authors':forms.CheckboxSelectMultiple(),
        }