# Generated by Django 4.2.5 on 2023-12-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0012_userhistory_is_returned'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfav',
            name='book_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userfav',
            name='image_url_l',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userfav',
            name='reference_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]