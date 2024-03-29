# Generated by Django 3.0.3 on 2020-04-22 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0002_auto_20200413_1353'),
        ('listings', '0003_auto_20200413_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.Staff'),
        ),
        migrations.AlterField(
            model_name='search',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
