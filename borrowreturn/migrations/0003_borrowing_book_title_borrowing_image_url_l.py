# Generated by Django 4.2.6 on 2023-10-29 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrowreturn', '0002_borrowing_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowing',
            name='book_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='borrowing',
            name='image_url_l',
            field=models.URLField(blank=True, null=True),
        ),
    ]