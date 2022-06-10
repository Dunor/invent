from django.contrib import admin

from .models import TypeOfficeEquipment


class TypeOfficeEquipmentAdmin(admin.ModelAdmin):
    radio_fields = {"interfaces": admin.HORIZONTAL}


admin.site.register(TypeOfficeEquipment, TypeOfficeEquipmentAdmin)

