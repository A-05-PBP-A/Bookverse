# Generated by Django 4.2.5 on 2023-12-05 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookProfile', '0002_auto_20231124_0231'),
        ('userProfile', '0013_userfav_book_title_userfav_image_url_l_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfav',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookProfile.book'),
        ),
    ]