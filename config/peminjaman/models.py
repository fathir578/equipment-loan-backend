from django.db import models
from django.conf import settings
from alat.models import Alat


User = settings.AUTH_USER_MODEL 

class peminjaman(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    alat = models.ForeignKey (Alat, on_delete=models.CASCADE)
    tanggal_pinjam = models.DateField(auto_now_add =True)
    tanggal_kemabali = models.DateField(null=True, blank=True)


def __str__(self):
    return f"{self.User} - {self.alat}" 


# Create your models here.
