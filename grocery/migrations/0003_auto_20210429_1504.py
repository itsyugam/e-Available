# Generated by Django 3.1.5 on 2021-04-29 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0002_auto_20210429_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Img',
            new_name='cateImg',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Name',
            new_name='cateName',
        ),
    ]
