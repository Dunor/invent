from django.contrib import admin

from .models import OfficeEquipment
from users.models import Owner


class OfficeEquipmentAdmin(admin.ModelAdmin):
    fields = (
        'equipe_type',
        'model',
        'sticker',
        'status',
        'item_number',
    )


admin.site.register(OfficeEquipment, OfficeEquipmentAdmin)

