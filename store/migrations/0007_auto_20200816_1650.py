# Generated by Django 3.0.4 on 2020-08-16 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20200816_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
