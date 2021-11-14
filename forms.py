from django import forms
from .models import Triplog


class TripForm(forms.ModelForm):
    class Meta:
        model = Triplog
        fields = ('title', 'content', 'latitude', 'longitude')

        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 50}),
            'latitude': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            'longitude': forms.Textarea(attrs={'rows': 1, 'cols': 30}),
            }
        
