# Generated by Django 5.1.6 on 2025-03-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asosiy', '0013_konfirensiya_publish_time_yangiliklar_publish_time_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='konfirensiya',
            options={'ordering': ['-boshlanish_sanasi'], 'verbose_name': 'Konfirensiya', 'verbose_name_plural': 'Konfirensiyalar'},
        ),
        migrations.AlterModelOptions(
            name='yangiliklar',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Yangiliklar'},
        ),
        migrations.AddField(
            model_name='tanlov',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True, default='2024-03-04 12:00'),
            preserve_default=False,
        ),
    ]
