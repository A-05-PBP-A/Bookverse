# Generated by Django 4.2.6 on 2023-11-28 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookProfile', '0002_auto_20231124_0231'),
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pengguna',
            name='booksHistory',
        ),
        migrations.RemoveField(
            model_name='pengguna',
            name='borrowedBooks',
        ),
        migrations.RemoveField(
            model_name='pengguna',
            name='favoriteBooks',
        ),
        migrations.RemoveField(
            model_name='pengguna',
            name='reviewsHistory',
        ),
        migrations.AddField(
            model_name='pengguna',
            name='booksHistory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books_history', to='bookProfile.book'),
        ),
        migrations.AddField(
            model_name='pengguna',
            name='borrowedBooks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to='bookProfile.book'),
        ),
        migrations.AddField(
            model_name='pengguna',
            name='favoriteBooks',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_books', to='bookProfile.book'),
        ),
        migrations.AddField(
            model_name='pengguna',
            name='reviewsHistory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_history', to='bookProfile.review'),
        ),
    ]
