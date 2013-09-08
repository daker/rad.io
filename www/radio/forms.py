# -*- coding: utf-8 -*-
from django import forms
from django.forms.widgets import *
from apps.mix.models import Artiste, Track


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artiste
        exclude = ('user', 'is_public', )


class MixUploadForm(forms.ModelForm):
    class Meta:
        model = Track
        exclude = ('artiste', 'is_public', 'votes', 'plays', 'is_featured')

    def clean(self):
        cleaned_data = self.cleaned_data

        if not 'file' in cleaned_data:
            raise forms.ValidationError('Merci de bien vouloir ajouter ta Mixtape!')

        if cleaned_data['file']:

            extension = cleaned_data['file'].name.lower().split('.')[-1]
            if extension not in ('mp3', 'ogg'):
                raise forms.ValidationError('Ta Mixtape a une format invalide (format autorisé : mp3, ogg).')

        return cleaned_data


class MixEditForm(forms.ModelForm):
    class Meta:
        model = Track
        exclude = ('artiste', 'is_public', 'votes', 'plays', 'is_featured')


class ContactForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate[required]'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'validate[required]'}))
    topic = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate[required]'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'validate[required]'}))
