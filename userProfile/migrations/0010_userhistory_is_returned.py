# Generated by Django 4.2.5 on 2023-12-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0009_userhistory_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='userhistory',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
    ]
