# Generated by Django 4.2.11 on 2024-04-17 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playerapp', '0018_mlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mlist',
            name='song3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playerapp.movieplaylistadd'),
        ),
    ]
