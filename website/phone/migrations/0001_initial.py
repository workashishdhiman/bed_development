# Generated by Django 4.2.11 on 2024-05-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Category', models.CharField(max_length=2, verbose_name=(('WA', 'WashingMachine'), ('FR', 'Refridgerator'), ('CR', 'Camera'), ('MB', 'mobile'), ('TB', 'Tabs'), ('HE', 'HomeElectoronics'), ('SQ', 'Security')))),
                ('Date_of_Manufacture', models.DateField(default='Now()')),
                ('Serial_Number', models.CharField(max_length=10)),
                ('product_image', models.ImageField(upload_to='devices')),
            ],
        ),
    ]
