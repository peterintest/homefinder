# Generated by Django 3.0.3 on 2020-04-25 12:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20200422_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='search',
            name='search_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
