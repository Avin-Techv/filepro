import os
import magic
from .forms import ListFilesForm
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import FormView


# Create your views here.


class ListFiles(FormView):

    template_name = "file/listfiles.html"
    form_class = ListFilesForm
    success_url = '.'

    def form_valid(self, form):
        filepath=form.cleaned_data.get('file_path')
        path_valid = os.path.exists(filepath)

        if path_valid == True:
            if os.path.isdir(filepath):
                messages.add_message(self.request, messages.WARNING, 'The Entered Path is a valid folder. !')
            elif os.path.isfile(filepath):
                messages.add_message(self.request, messages.WARNING, 'The Entered Path is a file.')
                print('\n\n')
                messages.add_message(self.request, messages.WARNING, 'File Details')
                print('\n')
                messages.add_message(self.request, messages.WARNING, '============')
                print('\n')
                result = magic.from_file(filepath)
                messages.add_message(self.request, messages.WARNING, result)
        else:
            print("Entered path is not valid...")
            messages.add_message(self.request, messages.WARNING, 'Entered path is not valid !')
        return super(ListFiles, self).form_valid(form)
