# Generated by Django 4.0.5 on 2022-06-13 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_vote', '0002_alter_hotel_table_history_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history_winner',
            name='winner',
            field=models.CharField(max_length=255),
        ),
    ]