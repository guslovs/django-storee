# Generated by Django 5.1.2 on 2025-01-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_checkoutmodel_card_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkoutmodel',
            name='cvv',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkoutmodel',
            name='mmyy',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
