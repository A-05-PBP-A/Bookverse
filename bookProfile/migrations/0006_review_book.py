# Generated by Django 4.2.6 on 2023-10-28 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookProfile', '0005_rename_isbn_book_isbn_remove_review_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bookProfile.book'),
            preserve_default=False,
        ),
    ]
