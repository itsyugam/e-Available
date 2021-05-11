# Generated by Django 3.1.5 on 2021-05-11 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0010_auto_20210510_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='oId',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='Cate',
            field=models.CharField(choices=[('bodyCare', 'Body care'), ('kitchen', 'Kitchen ware'), ('electronic', 'Electronic'), ('clothing', 'Clothing')], max_length=100),
        ),
    ]
