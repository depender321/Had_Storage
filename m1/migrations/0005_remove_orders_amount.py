# Generated by Django 2.2.4 on 2020-02-01 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m1', '0004_auto_20200201_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='amount',
        ),
    ]
