# Generated by Django 4.2.5 on 2023-12-02 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0006_userborrowed_is_returned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userhistory',
            name='booksHistory',
        ),
        migrations.RemoveField(
            model_name='userhistory',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserBorrowed',
        ),
        migrations.DeleteModel(
            name='UserHistory',
        ),
    ]
