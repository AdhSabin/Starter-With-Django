# Generated by Django 5.0.6 on 2025-07-18 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Relation', '0003_book_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_images/'),
        ),
    ]
