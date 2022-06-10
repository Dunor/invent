from django.db import models

from technics.models import TypeOfficeEquipment
from users.models import Owner


class OfficeEquipment(models.Model):
    STATUSES = [
        ('in_work', 'В работе'),
        ('in_stock', 'На складе'),
        ('under_repair', 'В ремонте'),
    ]

    model = models.ForeignKey(TypeOfficeEquipment, max_length=30, 
                              verbose_name='модель', on_delete=models.DO_NOTHING,)
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING, null=True)
    sticker = models.CharField(max_length=10, verbose_name='стикер')
    item_number = models.CharField(max_length=30, verbose_name='инвентарный номер')
    status = models.CharField(max_length=15, choices=STATUSES, verbose_name='статус')