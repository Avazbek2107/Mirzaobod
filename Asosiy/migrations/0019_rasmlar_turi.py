# Generated by Django 5.1.6 on 2025-03-06 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0018_rasmlar_turlari'),
    ]

    operations = [
        migrations.AddField(
            model_name='rasmlar',
            name='turi',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Asosiy.rasmlar_turlari'),
            preserve_default=False,
        ),
    ]
