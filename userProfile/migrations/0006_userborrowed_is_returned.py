# Generated by Django 4.2.5 on 2023-12-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0005_userborrowed_book_title_userborrowed_image_url_l_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userborrowed',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
    ]
