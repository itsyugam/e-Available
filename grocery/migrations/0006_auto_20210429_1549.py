# Generated by Django 3.1.5 on 2021-04-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0005_auto_20210429_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Cate',
            field=models.CharField(choices=[('bodyCare', 'Body care'), ('kitchen', 'Kitchen ware')], max_length=100),
        ),
    ]
