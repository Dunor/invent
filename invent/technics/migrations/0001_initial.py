# Generated by Django 4.0.5 on 2022-06-16 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfficeEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equip_type', models.CharField(choices=[('mfu', 'МФУ'), ('printer', 'Принтер'), ('scanner', 'Сканер'), ('plotter', 'Плоттер')], max_length=15, verbose_name='тип устройства')),
                ('model', models.CharField(max_length=30, verbose_name='модель')),
                ('cartridge', models.ManyToManyField(to='extras.cartrige', verbose_name='картриджи')),
                ('interfaces', models.ManyToManyField(to='extras.interface', verbose_name='доступные интерфейсы')),
            ],
        ),
    ]
