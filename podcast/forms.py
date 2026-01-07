from django import forms
from .models import Podcast, Reel


class PodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ["titulo", "archivo_audio", "descripcion", "evento"]


class ReelForm(forms.ModelForm):
    class Meta:
        model = Reel
        fields = ["titulo", "video", "miniatura", "evento"]
