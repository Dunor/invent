# Generated by Django 4.0.3 on 2022-03-24 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technics', '0004_remove_officeequipment_cabinet_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='officeequipment',
            options={'verbose_name': 'оргтехника', 'verbose_name_plural': 'оргтехника'},
        ),
        migrations.RenameField(
            model_name='officeequipment',
            old_name='equipe_type',
            new_name='equip_type',
        ),
    ]