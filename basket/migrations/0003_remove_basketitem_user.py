# Generated by Django 4.2.11 on 2024-05-09 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_basketitem_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basketitem',
            name='user',
        ),
    ]
