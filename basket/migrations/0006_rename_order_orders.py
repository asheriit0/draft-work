# Generated by Django 4.2.11 on 2024-05-26 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_remove_basketitem_total_price_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
    ]
