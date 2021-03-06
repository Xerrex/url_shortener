from django import forms
from .models import ShortUrl

class NewShortUrlForm(forms.ModelForm):
    
    class Meta:
        model = ShortUrl
        fields = ['original_url'] # https://example.com
