from django import forms
from .models import Image
from django.contrib.auth.forms import UserCreationForm
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout, ButtonHolder, Submit
#from django.forms.widgets import FileInput


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('img',)