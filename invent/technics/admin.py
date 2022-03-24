from django.contrib import admin

from .models import OfficeEquipment, TypeOfficeEquipment
from users.models import Owner


class OfficeEquipmentAdmin(admin.ModelAdmin):
    # fields = (
    #     'equipe_type',
    #     'model',
    #     'sticker',
    #     'status',
    #     'item_number',
    # )
    pass


admin.site.register(OfficeEquipment, OfficeEquipmentAdmin)
admin.site.register(TypeOfficeEquipment)

