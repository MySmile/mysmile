import os
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

from django.test import TestCase
from django.conf import settings
from apps.preferences.models import PreferencesManager


class SignalsTestCase(TestCase):
    fixtures = ['preferences.json']

    def setUp(self):
        pass

    def test_email2img(self):
        p = PreferencesManager().get_all()
        email = p.get('EMAIL')
        color_mode = "RGBA"
        background_color = (0, 0, 0, 0)  # full transparent
        fontfile = os.path.join(settings.STATIC_ROOT, 'fonts/TimesNewRomanCE.ttf')
        fontsize = 16
        textcolor = (119 , 119, 119)

        font = ImageFont.truetype(fontfile, fontsize)
        width, height = font.getsize(email)

        file = BytesIO()
        image = Image.new(color_mode, (width, height + fontsize % 10), background_color)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), email, textcolor, font=font)
        image.save(file, 'png')
        file.name = 'testemail.png'
        file.seek(0)

        self.assertTrue(isinstance(file.read(), bytes))

    def test_clear_photo_file(self):
        pass

