from django.db import models

# Create your models here.


class Exclude(models.Model):
    txt = '.txt'
    jpg = '.jpg'

    FILE_TYPES = ((txt, '.txt'),
                  (jpg, '.jpg'),
                  )

    root = models.URLField(label='URL :')
    exclusion_types = models.CharField(default='', choices='FILE_')

    def __str__(self):
        return self.root

