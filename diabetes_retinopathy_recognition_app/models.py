# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Image(models.Model):
    img = models.ImageField(upload_to='images/', verbose_name="Image:",
                            default = 'images/None/no-img.jpg')