# Generated by Django 2.2.4 on 2020-02-01 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m1', '0005_remove_orders_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
