# Generated by Django 4.2.6 on 2023-10-29 08:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daftar_buku', '0002_alter_main_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='date',
        ),
        migrations.AddField(
            model_name='main',
            name='current_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
