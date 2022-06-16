from django.db import models

from django.db import models
from users.models import Owner
from extras.models import Interface, Cartrige


# TYPE_CHOICES = [
#     ('mfu', 'МФУ'),
#     ('printer', 'Принтер'),
#     ('scaner', 'Сканер'),
#     ('monitor', 'Монитор'),
#     ('sb', 'Системный блок'),
#     ('monoblock', 'Моноблок'),
#     ('mfu', 'Планшет'),
# ]



class TypeOfficeEquipment(models.Model):
    TYPE_CHOICES = [
        ('mfu', 'МФУ'),
        ('printer', 'Принтер'),
        ('scanner', 'Сканер'),
        ('plotter', 'Плоттер'),
    ]

    INTERFACE_CHOICES = [
        ('usb', 'USB'),
        ('ethernet', 'Ethernet'),
        ('wifi', 'wi-fi'),
    ]
    equip_type = models.CharField(max_length=15, choices=TYPE_CHOICES,
                                  verbose_name='тип устройства')
    model = models.CharField(max_length=30, verbose_name='модель')
    cartridge = models.ManyToManyField(Cartrige, verbose_name='картриджи')
    interfaces = models.ManyToManyField(Interface,
                                        verbose_name='доступные интерфейсы')


    def __str__(self):
        return self.model
