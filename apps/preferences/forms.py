import os
from django import forms
from django.forms import ModelForm
from django.conf import settings

from apps.preferences.models import Preferences

# import re
# SHIELD_SYMBOLS = r'[#=!?*]'


class PreferencesForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PreferencesForm, self).__init__(*args, **kwargs)
        if self.initial:
            self.fields['key'].label = ''
            self.fields['key'].widget.attrs = {'readonly': 'readonly', 'style': 'display: none;'}
            self.fields['description'].widget = forms.Textarea()
            self.fields['description'].widget.attrs = {'rows': 3, 'cols': 100, 'readonly': True,
                                                      'style': 'resize: none;'}

        if Preferences.KEY_REST_API in self.initial['key']:
            self.fields['value'].widget = forms.Select(choices=((True, 'True'), (False, 'False')))
        if Preferences.KEY_IMAGE_AUTOSCALE in self.initial['key']:
            self.fields['value'].widget = forms.Select(choices=((True, 'True'), (False, 'False')))

        if Preferences.KEY_MAX_INNERLINK_HISTORY in self.initial['key']:
            self.fields['value'].widget = forms.NumberInput()

        if Preferences.KEY_IMAGE_QUALITY in self.initial['key']:
            choices = tuple((str(i), str(i)) for i in range(100, 0, -10))
            self.fields['value'].widget = forms.Select(choices=choices)

        if Preferences.KEY_THEME in self.initial['key']:
            path_of_themes = os.path.join(settings.BASE_DIR, 'apps/pages/templates/themes/')
            choices = ((name, name) for name in os.listdir(path_of_themes)
                       if os.path.isdir(os.path.join(path_of_themes, name)))

            self.fields['value'].widget = forms.Select(choices=choices)


    class Meta:
        model = Preferences
        exclude = ['updated_at', 'created_at']

    #~ def clean_value(self):
        #~ new_value = self.cleaned_data['value']
        #~ match = re.search(SHIELD_SYMBOLS, new_value)
        #~ if match:
            #~ raise forms.ValidationError("Don\'t use symbols #=!?* ")
        #~ return new_value
