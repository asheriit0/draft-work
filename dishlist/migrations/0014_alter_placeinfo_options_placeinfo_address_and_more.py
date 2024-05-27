# Generated by Django 4.2.11 on 2024-05-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishlist', '0013_alter_place_options_placeinfo_place_place_info'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeinfo',
            options={'verbose_name': 'Информация о заведении', 'verbose_name_plural': 'Информация о заведениях'},
        ),
        migrations.AddField(
            model_name='placeinfo',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='placeinfo',
            name='average_check',
            field=models.PositiveIntegerField(null=True, verbose_name='Средний чек'),
        ),
        migrations.AddField(
            model_name='placeinfo',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='placeinfo',
            name='inn',
            field=models.PositiveIntegerField(null=True, unique=True, verbose_name='ИНН'),
        ),
        migrations.AddField(
            model_name='placeinfo',
            name='number_of_tables',
            field=models.PositiveIntegerField(null=True, verbose_name='Количество столиков'),
        ),
        migrations.AddField(
            model_name='placeinfo',
            name='organization_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Название организации'),
        ),
        migrations.AddField(
            model_name='placeinfo',
            name='working_hours',
            field=models.CharField(max_length=255, null=True, verbose_name='Часы работы'),
        ),
    ]
