# Generated by Django 5.1.4 on 2024-12-17 15:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(error_messages={'blank': 'This field is required', 'max_length': 'This field must not exceed 255 characters'}, max_length=255, validators=[django.core.validators.RegexValidator(message='First Name can only contain letters, spaces, hyphens, and must start and end with a letter', regex='(^[A-Za-z]{1,255}$)|(^[A-Za-z]{1,}[\\s\\-]{1}[A-Za-z]{1,253}$)')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(error_messages={'blank': 'This field is required', 'max_length': 'This field must not exceed 255 characters'}, max_length=255, validators=[django.core.validators.RegexValidator(message='First Name can only contain letters, spaces, hyphens, and must start and end with a letter', regex='(^[A-Za-z]{1,255}$)|(^[A-Za-z]{1,}[\\s\\-]{1}[A-Za-z]{1,253}$)')]),
        ),
    ]
