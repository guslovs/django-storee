# Generated by Django 5.1.2 on 2025-01-14 15:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_checkoutmodel_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutmodel',
            name='card_number',
            field=models.IntegerField(blank=True, null=True, verbose_name=django.core.validators.MaxValueValidator(16)),
        ),
    ]
