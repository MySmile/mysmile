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
        js = ('jscolor/jscolor.js',)
        #css = {
            #'all': ('zzzZZZzzz.css',)
        #}

    # def clean_photo(self):
    #     new_photo = self.cleaned_data['photo']
    #     self.
    #     if new_photo != self.old_photo:
    #         from PIL import Image
    #         path = new_photo
    #         image = Image.open(path)
    #         image.save(path,quality=20,optimize=True)
    #         print('PHOTO UPDATE')
    #     else:
    #         print('NOT_NOT-NOT')
    #
    #     return new_photo
