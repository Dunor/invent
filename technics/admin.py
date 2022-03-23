from django.contrib import admin

from .models import OfficeEquipment, Owner


class OfficeEquipmentAdmin(admin.ModelAdmin):
    fields = (
        'equipe_type',
        'model',
        'owner',
        'cabinet',
        'sticker',
        'status',
        'item_number',
    )


admin.site.register(OfficeEquipment, OfficeEquipmentAdmin)
admin.site.register(Owner)
