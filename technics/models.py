from django.db import models

from django.db import models


# TYPE_CHOICES = [
#     ('mfu', 'МФУ'),
#     ('printer', 'Принтер'),
#     ('scaner', 'Сканер'),
#     ('monitor', 'Монитор'),
#     ('sb', 'Системный блок'),
#     ('monoblock', 'Моноблок'),
#     ('mfu', 'Планшет'),
# ]
class Owner(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    cabinet = models.CharField(max_length=50, verbose_name='кабинет')

    def __str__(self):
        return self.name


class BaseTech(models.Model):
    STATUSES = [
        ('in_work', 'В работе'),
        ('in_stock', 'На складе'),
        ('under_repair', 'В ремонте'),
    ]

    model = models.CharField(max_length=30, verbose_name='модель')
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING, null=True)
    cabinet = models.IntegerField(verbose_name='кабинет')
    sticker = models.CharField(max_length=10, verbose_name='стикер')
    item_number = models.CharField(max_length=30, verbose_name='инвентарный номер')
    status = models.CharField(max_length=15, choices=STATUSES, verbose_name='статус')

    class Meta:
        abstract = True


class OfficeEquipment(BaseTech):
    TYPE_CHOICES = [
        ('mfu', 'МФУ'),
        ('printer', 'Принтер'),
        ('scaner', 'Сканер'),
        ('plotter', 'Плоттер'),
    ]
    equipe_type = models.CharField(max_length=15, choices=TYPE_CHOICES, verbose_name='тип устройства')
    cartrige = models.CharField(max_length=50, verbose_name='картриджи')
    connection_interfaces = models.CharField(max_length=50, verbose_name='доступные интерфейсы')
    mac_addres = models.CharField(max_length=50, verbose_name='MAC-адрес')
    ip_address = models.CharField(max_length=50, verbose_name='IP-адрес')
    net_name = models.CharField(max_length=50, verbose_name='сетевое имя')



