from django.db import models

from django.db import models
from users.models import Owner


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
    cartridge = models.CharField(max_length=50, verbose_name='картриджи')
    interfaces = models.CharField(max_length=50, choices=INTERFACE_CHOICES,
                                  verbose_name='доступные интерфейсы')

