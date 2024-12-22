from django import forms
from .models import Signature

class SignatureForm(forms.ModelForm):
    class Meta:
        model = Signature
        fields = ['original_image', 'uploaded_image']
