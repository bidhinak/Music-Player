# Generated by Django 4.2.11 on 2024-04-09 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playerapp', '0015_movieplaylistadd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlistadd',
            name='user',
        ),
    ]
