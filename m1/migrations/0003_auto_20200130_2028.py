# Generated by Django 2.2.4 on 2020-01-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m1', '0002_auto_20200130_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.IntegerField(verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='zipcode',
            field=models.IntegerField(verbose_name='zipcode'),
        ),
    ]
