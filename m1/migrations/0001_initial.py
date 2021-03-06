# Generated by Django 2.2.7 on 2020-01-30 09:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sb_price', models.IntegerField()),
                ('mb_price', models.IntegerField()),
                ('lb_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=10, verbose_name='fname')),
                ('lname', models.CharField(max_length=10, verbose_name='lname')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.CharField(max_length=10, verbose_name='phone')),
                ('message', models.CharField(max_length=100, verbose_name='message')),
            ],
            options={
                'verbose_name_plural': 'contactus',
            },
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('orders_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('sbox', models.IntegerField(verbose_name='sbox')),
                ('mbox', models.IntegerField(verbose_name='mbox')),
                ('lbox', models.IntegerField(verbose_name='lbox')),
                ('month', models.IntegerField(verbose_name='month')),
                ('amount', models.IntegerField(default=0, verbose_name='amount')),
                ('name', models.CharField(max_length=10, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.CharField(max_length=10, verbose_name='phone')),
                ('pickup_location', models.CharField(max_length=100, verbose_name='pickup_location')),
                ('zipcode', models.CharField(max_length=10, verbose_name='zipcode')),
                ('date', models.DateField(default=datetime.date.today)),
                ('hour', models.IntegerField(verbose_name='hour')),
                ('minutes', models.IntegerField(verbose_name='minutes')),
                ('username', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='feedbacks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=1000, verbose_name='msg')),
                ('username', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'feedback',
            },
        ),
    ]
