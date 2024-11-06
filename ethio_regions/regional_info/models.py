from django.db import models

# Create your models here.

class RegionalInfo(models.Model):
    region_number=models.PositiveSmallIntegerField()
    region_name=models.CharField(max_length=200)
    population_size=models.PositiveBigIntegerField()
    area=models.FloatField()
    capital_city=models.CharField(max_length=200)
    flag=models.ImageField(upload_to='flag')
    email=models.EmailField()
    map=models.ImageField(upload_to='map')
    website=models.URLField()
    