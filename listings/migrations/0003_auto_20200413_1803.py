# Generated by Django 3.0.3 on 2020-04-13 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_search'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='search',
            options={'verbose_name_plural': 'searches'},
        ),
    ]