# Generated by Django 5.1.4 on 2024-12-17 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('user_shipping_details', '0002_remove_usershippingdetails_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usershippingdetails',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cities_light.city'),
        ),
        migrations.AlterField(
            model_name='usershippingdetails',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cities_light.country'),
        ),
    ]
