from django.forms import ModelForm

from apps.pages.models import Page_translation, Page


class Page_translationInlineForm(ModelForm):
    class Meta:
        model = Page_translation
        exclude = ['updated_at', 'created_at']


class PageForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        self.fields['color'].widget.attrs = {'class': "color {hash:true,caps:false}"}

    class Meta:
        model = Page
        exclude = ['updated_at', 'created_at']

    class Media:
        js = ('vendor/jscolor/jscolor.js',)
        #css = {
            #'all': ('zzzZZZzzz.css',)
        #}
