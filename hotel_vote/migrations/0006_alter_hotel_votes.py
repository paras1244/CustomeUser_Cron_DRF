# Generated by Django 4.0.5 on 2022-06-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_vote', '0005_history_winner_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='votes',
            field=models.FloatField(default=0),
        ),
    ]
