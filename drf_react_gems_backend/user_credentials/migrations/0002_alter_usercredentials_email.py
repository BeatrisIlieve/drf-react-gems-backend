# Generated by Django 5.1.4 on 2024-12-15 14:39

import drf_react_gems_backend.user_credentials.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_credentials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercredentials',
            name='email',
            field=models.CharField(error_messages={'unique': 'This email address is already registered'}, max_length=255, unique=True, validators=[drf_react_gems_backend.user_credentials.models.CustomEmailValidator()]),
        ),
    ]
