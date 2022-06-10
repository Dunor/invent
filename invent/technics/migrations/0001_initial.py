# Generated by Django 4.0.5 on 2022-06-08 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sticker', models.CharField(max_length=10, verbose_name='стикер')),
                ('item_number', models.CharField(max_length=30, verbose_name='инвентарный номер')),
                ('status', models.CharField(choices=[('in_work', 'В работе'), ('in_stock', 'На складе'), ('under_repair', 'В ремонте')], max_length=15, verbose_name='статус')),
                ('equip_type', models.CharField(choices=[('mfu', 'МФУ'), ('printer', 'Принтер'), ('scanner', 'Сканер'), ('plotter', 'Плоттер')], max_length=15, verbose_name='тип устройства')),
                ('model', models.CharField(max_length=30, verbose_name='модель')),
                ('cartridge', models.CharField(max_length=50, verbose_name='картриджи')),
                ('interfaces', models.CharField(max_length=50, verbose_name='доступные интерфейсы')),
                ('mac_address', models.CharField(max_length=50, verbose_name='MAC-адрес')),
                ('ip_address', models.CharField(max_length=50, verbose_name='IP-адрес')),
                ('net_name', models.CharField(max_length=50, verbose_name='сетевое имя')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.owner')),
            ],
            options={
                'verbose_name': 'оргтехника',
                'verbose_name_plural': 'оргтехника',
            },
        ),
    ]
