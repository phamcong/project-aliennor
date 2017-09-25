import datetime
from django import forms
from .models import EcoCase
from tinymce.widgets import TinyMCE
from django.contrib.admin import widgets
from django.contrib.auth import authenticate


class EcoCaseForm(forms.ModelForm):
    ecocase_title = forms.CharField(max_length=200)
    ecocase_description = forms.CharField(widget=TinyMCE(
        attrs={'rows': 4, 'cols': 100}), max_length=300)
    ecocase_characters = forms.CharField(
        widget=TinyMCE(attrs={'rows': 100, 'cols': 500}))
    ecocase_images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = EcoCase
        fields = ('ecocase_title', 'ecocase_description',
                  'ecocase_characters', 'ecocase_images')
    # ecocase_title = forms.CharField(max_length=200)
    # ecocase_description = forms.CharField(widget=forms.Textarea, max_length=300)
    # ecocase_characters = forms.CharField(widget=forms.Textarea, max_length=5000)
    # ecocase_image_urls = forms.CharField(max_length=None)
    # ecocase_images = forms.FileField()
    # pub_date = forms.DateTimeField('date published')


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
