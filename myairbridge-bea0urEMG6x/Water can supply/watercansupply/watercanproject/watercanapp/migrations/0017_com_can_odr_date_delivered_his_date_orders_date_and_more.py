# Generated by Django 4.1.7 on 2023-04-21 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watercanapp', '0016_remove_com_can_odr_com_can_remove_delivered_his_delv_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='com_can_odr',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='delivered_his',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='usr_can_odr',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
