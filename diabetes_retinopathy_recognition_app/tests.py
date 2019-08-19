# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Image
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.conf import settings

class ImageTestCase(TestCase):

    def test_images(self):
            self.assertNotIn("test.png", os.listdir(settings.MEDIA_ROOT))
            self.assertEqual(Image.objects.all().count(), 0)

            media_file = SimpleUploadedFile("test.png", b"\x00\x01\x02\x03")
            image = Image(img=media_file)
            image.save()

            self.assertEqual(Image.objects.all().count(), 1)
