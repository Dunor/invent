from django.db import models


class Owner(models.Model):
    fname = models.CharField(max_length=50, verbose_name='имя')
    lname = models.CharField(max_length=50, verbose_name='фамилия')
    mname = models.CharField(max_length=50, verbose_name='отчество')

    def __str__(self):
        return f'{self.lname} {self.fname[0]}.{self.mname[0]}.'
