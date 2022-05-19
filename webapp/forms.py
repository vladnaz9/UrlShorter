from .models import UrlShorter
from django.forms import TextInput, ModelForm


class ShortUrlForm(ModelForm):
    # long_url = forms.URLField(widget=forms.URLInput(
    #     attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))

    class Meta:
        model = UrlShorter
        fields = ['long_url']
        widgets = {'long_url': TextInput(attrs={
            'class': 'form-control',
            'name': 'long_url',
            'id': 'long_url',
            'placeHolder': 'your url here',
        })
        }

