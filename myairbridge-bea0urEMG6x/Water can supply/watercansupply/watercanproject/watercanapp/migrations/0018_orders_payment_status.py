# Generated by Django 4.1.7 on 2023-04-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watercanapp', '0017_com_can_odr_date_delivered_his_date_orders_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]