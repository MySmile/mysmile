from django import forms 
from django.forms import ModelForm

from apps.pages.models import Page_translation, Page


class Page_translationInlineForm(ModelForm):

    class Meta:
        model = Page_translation
        exclude = ['updated_at', 'created_at']


class PageForm(ModelForm):

    class Meta:
        model = Page
        exclude = ['updated_at', 'created_at']
