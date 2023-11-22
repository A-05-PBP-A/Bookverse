# Generated by Django 4.2.6 on 2023-10-27 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookProfile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(blank=True, max_length=13, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('publication_year', models.IntegerField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('image_url_s', models.URLField(blank=True, null=True)),
                ('image_url_m', models.URLField(blank=True, null=True)),
                ('image_url_l', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
