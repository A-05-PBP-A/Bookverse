# Generated by Django 4.2.6 on 2023-10-29 09:07

from django.db import migrations

def update_review_names(apps, schema_editor):
    Review = apps.get_model('bookProfile', 'Review')
    for review in Review.objects.all():
        review.name = review.user.username
        review.save()

class Migration(migrations.Migration):

    dependencies = [
        ('bookProfile', '0011_review_name'),
    ]

    operations = [
        migrations.RunPython(update_review_names),
    ]
