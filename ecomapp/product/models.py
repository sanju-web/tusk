from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    qty=models.IntegerField()
    category=models.CharField(max_length=50)
    remarks=models.CharField(max_length=50)
    brand=models.CharField(max_length=50)
    vendor=models.CharField(max_length=50)

    class Meta:
        db_table='Product_Info'
