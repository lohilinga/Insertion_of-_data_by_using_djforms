from django import forms
from app.models import *

class Topic_form(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class Webpage_form(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
    




