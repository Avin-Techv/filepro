from django.db import models

# Create your models here.


class Exclude(models.Model):

    root = models.URLField(max_length=100)
    exclusion_types = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.root
