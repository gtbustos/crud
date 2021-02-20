from django.db import models


class Alvo(models.Model):
    nome = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    validade = models.DateField()
