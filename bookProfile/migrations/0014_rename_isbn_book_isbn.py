# Generated by Django 4.2.6 on 2023-11-23 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookProfile', '0013_remove_book_isbn_book_isbn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='ISBN',
            new_name='isbn',
        ),
    ]
