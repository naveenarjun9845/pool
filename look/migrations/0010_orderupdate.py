# Generated by Django 3.1.3 on 2020-12-23 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('look', '0009_auto_20201222_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
