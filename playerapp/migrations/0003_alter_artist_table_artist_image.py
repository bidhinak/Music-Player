# Generated by Django 5.0.1 on 2024-03-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playerapp', '0002_artist_table_artist_image_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist_table',
            name='artist_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
