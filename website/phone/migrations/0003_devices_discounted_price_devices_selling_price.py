# Generated by Django 4.2.11 on 2024-05-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_alter_devices_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='Discounted_Price',
            field=models.FloatField(default='0'),
        ),
        migrations.AddField(
            model_name='devices',
            name='Selling_Price',
            field=models.FloatField(default='0'),
        ),
    ]
