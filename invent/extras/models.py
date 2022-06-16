from unicodedata import name
from django.db import models

class Interface(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False)

    def __str__(self) -> str:
        return self.name


class Cartrige(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False)

    def __str__(self) -> str:
        return self.name