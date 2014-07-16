from django import forms 
from django.forms import ModelForm

from apps.pages.models import Page_translation, Page, Settings

import re
SHIELD_SYMBOLS = r'[#=!?*]'


class Page_translationInlineForm(ModelForm):

    class Meta:
        model = Page_translation
        exclude = ['updated_at', 'created_at']


class PageForm(ModelForm):

    class Meta:
        model = Page
        exclude = ['updated_at', 'created_at']


class SettingsForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        if self.initial:
            self.fields['name'].widget.attrs['readonly'] = 'readonly'
            self.fields['description'].label = ''
            self.fields['description'].widget = forms.Textarea()
            self.fields['description'].widget.attrs= {'rows':3, 'cols':100,
                                                      'readonly': True, 'style':'resize:none;'}

    
        #~ if 'rest_api' in self.initial.keys():
            #~ print('------->>', self.initial.keys())
            #~ self.fields['value'].widget = forms.Select(choices = ((True,'True'), (False,'False'))) 
                     


    class Meta:
        model = Settings
        exclude = ['updated_at', 'created_at']

    #~ def clean_value(self):
        #~ new_value = self.cleaned_data['value']
        #~ match = re.search(SHIELD_SYMBOLS, new_value)
        #~ if match:
            #~ raise forms.ValidationError("Don\'t use symbols #=!?* ")
        #~ return new_value
