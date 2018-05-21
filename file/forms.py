from django import forms
from .models import Exclude


class ListFilesForm(forms.ModelForm):
    file_path = forms.CharField(max_length=50)

    class Meta:
            model = Exclude
            fields = ['file_path']
