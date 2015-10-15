from django.forms import ModelForm

from apps.pages.models import Page_translation, Page
from apps.preferences.models import Preferences

class Page_translationInlineForm(ModelForm):
    class Meta:
        model = Page_translation
        exclude = ['updated_at', 'created_at']


class PageForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        """ Temporary disable color field for non-classic themes. TODO: fix this in future.
        """
        self.theme = Preferences.objects.filter(key='THEME').values_list('value', flat=True)[0]
        if self.theme=='classic':
            self.fields['color'].widget.attrs = {'class': "color {hash:true,caps:false}"}
        else:
            # set default color
            self.fields['color'].widget.attrs = {'readonly':'readonly',
                                                 'value': self.Meta.model._meta.get_field('color').get_default()}

    class Meta:
        model = Page
        exclude = ['updated_at', 'created_at']

    class Media:
        js = ('vendor/jscolor/jscolor.js',)
        #css = {
            #'all': ('zzzZZZzzz.css',)
        #}

