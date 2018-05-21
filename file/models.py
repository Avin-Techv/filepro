from django.db import models

# Create your models here.


class Exclude(models.Model):

    file_path = models.CharField(max_length=255)

