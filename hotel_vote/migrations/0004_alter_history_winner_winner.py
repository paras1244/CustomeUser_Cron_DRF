# Generated by Django 4.0.5 on 2022-06-13 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_vote', '0003_alter_history_winner_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history_winner',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_vote.hotel'),
        ),
    ]