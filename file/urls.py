from django.urls import path
from .views import ListFiles
app_name = 'file'

urlpatterns = [
    path('', ListFiles.as_view(), name="home")
    ]
