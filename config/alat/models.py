from django.db import models

class kategori (models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama
class Alat (models.Model):
    name = models.CharField(max_length=100)
    stok = models.IntegerField()
    kategori = models.ForeignKey(
        kategori,
        on_delete=models.CASCADE,
        related_name='alat'
    )
# Create your models here.