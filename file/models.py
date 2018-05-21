from django.db import models

# Create your models here.


class Exclude(models.Model):

    file_path = models.CharField(max_length=100)

    def __str__(self):
        return self.file_path
