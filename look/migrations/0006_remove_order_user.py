# Generated by Django 3.1.3 on 2020-12-22 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('look', '0005_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
