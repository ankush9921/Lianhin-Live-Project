from django.db import models
from lianhin.basecontent import BaseContent

# Create your models here.

class Surfacefinish(BaseContent):
    surface_name = models.CharField(max_length=255)
    icon = models.FileField(upload_to='surface',blank=True,null=True)

class Brand(BaseContent):
    brand_name = models.CharField(max_length=255)
    brand_image = models.FileField(upload_to='brand',blank=True,null=True)


class Collection(BaseContent):
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)
    collection_name = models.CharField(max_length=255)

class Series(BaseContent):
    collection = models.ForeignKey(to=Collection, on_delete=models.CASCADE)
    series_name = models.CharField(max_length=255)

class Model(BaseContent):
    series = models.ForeignKey(to=Series, on_delete=models.CASCADE)
    surfacefinish = models.OneToOneField(to=Surfacefinish, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=255)
    model_image = models.FileField(upload_to='model',blank=True,null=True)

