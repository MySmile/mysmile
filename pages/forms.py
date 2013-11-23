from django.forms import ModelForm
from django import forms
from pages.models import Page_translation

class Page_translationForm(ModelForm):
    class Meta:
        model = Page_translation
        exclude = ['updated_at', 'created_at']
