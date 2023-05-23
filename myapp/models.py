from django.db import models

class Vehicles(models.Model):
    name=models.CharField(max_length=250)
    model=models.CharField(max_length=200)
    category=models.CharField(max_length=230)
    owner=models.CharField(max_length=200)
    fuel_type=models.CharField(max_length=200)
    kms=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=2550)
    number=models.CharField(max_length=200,unique=True)

    def __str__(self) -> str:
        return self.name
    
class Mobiles(models.Model):
    name=models.CharField(max_length=200,unique=True)
    brand=models.CharField(max_length=200)
    price=models.PositiveSmallIntegerField()
    display=models.CharField(max_length=200,default="LCD")

    def __str__(self) -> str:
        return self.name
    

class Movies(models.Model):
    name=models.CharField(max_length=200,unique=True)
    genres=models.CharField(max_length=200)
    year=models.PositiveSmallIntegerField()
    language=models.CharField(max_length=200,default="malayalam")
    rating=models.FloatField(max_length=200)

    def __str__(self) -> str:
        return self.name
