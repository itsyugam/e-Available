# Generated by Django 3.1.5 on 2021-05-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0006_auto_20210429_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='id',
        ),
        migrations.AddField(
            model_name='products',
            name='Id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]