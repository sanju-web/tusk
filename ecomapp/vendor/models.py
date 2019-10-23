from django.db import models

# Create your models here.

class ActiveVendors(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active='YES')


class InActiveVendors(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active='NO')


class Vendor(models.Model):
    name=models.CharField(max_length=50)
    active=models.CharField(max_length=50,default='YES')
    allven=models.Manager()
    actven=ActiveVendors()
    iactven=InActiveVendors()

    class Meta:
        db_table='Vendor_Info'

# v1=Vendor(id=101,name='sanjay',active='YES')
