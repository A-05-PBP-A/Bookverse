# Generated by Django 4.2.6 on 2023-10-27 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookProfile', '0004_auto_20231027_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='ISBN',
            new_name='isbn',
        ),
    ]
