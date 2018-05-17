from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import get_user_model
from .forms import ListFilesForm

# Create your views here.


class ListFiles(FormView):
    template_name = "file/listfiles.html"
    form_class = ListFilesForm
    success_url = 'accounts/base.html'

    def form_valid(self, form):
        get_user_model().objects.create_user(form.cleaned_data.get('root'),
                                             form.cleaned_data.get('exclusion_types'),
                                             )
        return render(self.request, "file/listfiles.html")
