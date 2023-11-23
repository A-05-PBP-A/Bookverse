# Generated by Django 4.2.6 on 2023-10-27 05:13

from django.db import migrations
from django.core.management import call_command


def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "books_data.json")


class Migration(migrations.Migration):

    dependencies = [
        ('bookProfile', '0001_initial'),
    ]

    operations = [
         migrations.RunPython(load_my_initial_data),

    ]
