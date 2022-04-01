from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name


class Fruit(models.Model):
    region = models.ForeignKey(Region, related_name='Fruta', on_delete=models.CASCADE)
    nameFruit = models.CharField(max_length=255)


    class Meta:
        verbose_name = 'Fruit'
        verbose_name_plural = 'Fruits'
        unique_together = ['region', 'nameFruit']

    def __str__(self):
        return f'A fruta {self.nameFruit} esta ligada a região {self.region}'
