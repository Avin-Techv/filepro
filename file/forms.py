from django import forms
from .models import Exclude


class ListFilesForm(forms.ModelForm):
    root = forms.CharField(max_length=50)
    exclusion_types = forms.CharField(max_length=50)

    class Meta:
            model = Exclude
            fields = ['root', 'exclusion_types']
