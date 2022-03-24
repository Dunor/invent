from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    cabinet = models.CharField(max_length=50, verbose_name='кабинет')

    def __str__(self):
        return self.name
