from django.db import models

# Create your models here.
class Book(models.Model):
    catchoices=(("autobirography","autobirography"),("literature","literature"))
    bid=models.IntegerField()
    bname=models.CharField(max_length=20)
    authorname=models.CharField(max_length=20)
    publishdate=models.DateField()
    price=models.FloatField()
    

