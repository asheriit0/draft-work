# Generated by Django 4.2.11 on 2024-04-29 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dishlist', '0004_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishes',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dish_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
