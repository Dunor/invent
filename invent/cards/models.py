from django.db import models

from technics.models import TypeOfficeEquipment
from users.models import Owner


class OfficeEquipment(models.Model):
    STATUSES = [
        ('in_work', 'В работе'),
        ('in_stock', 'На складе'),
        ('under_repair', 'В ремонте'),
    ]

    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING, null=True)
    model = models.ForeignKey(TypeOfficeEquipment, max_length=30, 
                              verbose_name='модель', on_delete=models.DO_NOTHING,)
    interface = models.CharField(max_length=250, verbose_name='интерфейс подключения')
    sticker = models.CharField(max_length=10, verbose_name='стикер')
    item_number = models.CharField(max_length=30, verbose_name='инвентарный номер')
    status = models.CharField(max_length=15, choices=STATUSES, verbose_name='статус')
    mac_address = models.CharField(max_length=60, verbose_name='MAC-адрес')
    ip_address = models.IntegerField(verbose_name='IP-адрес')
    nat_name = models.CharField(max_length=60, verbose_name='сетевое имя')
    ceate_date = models.DateField(verbose_name='дата создания')
    comments = models.TextField(max_length=250, verbose_name='комментарий')
    cabinet = models.IntegerField(verbose_name='кабинет')