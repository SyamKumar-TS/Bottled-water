# Generated by Django 4.1.7 on 2023-02-26 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watercanapp', '0012_usr_can_odr_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='com_can_odr',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='delivered_his',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]