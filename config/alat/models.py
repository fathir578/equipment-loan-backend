from django.db import models

class kategori (models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
# Create your models here.
