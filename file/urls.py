from django.urls import path
from . import views

app_name = 'file'

urlpatterns = [
    path('', views.ListFiles.as_view(), name="home")
    ]
