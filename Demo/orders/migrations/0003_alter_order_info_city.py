# Generated by Django 3.2.9 on 2022-01-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20220114_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_info',
            name='city',
            field=models.CharField(default='TPE', max_length=100),
        ),
    ]
