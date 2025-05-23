# Generated by Django 5.1.6 on 2025-03-31 04:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_car_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdate', models.DateField()),
                ('ddate', models.DateField()),
                ('time', models.TimeField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
