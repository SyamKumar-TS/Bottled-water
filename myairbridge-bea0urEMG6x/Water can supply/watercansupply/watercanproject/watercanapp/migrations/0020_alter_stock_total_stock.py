# Generated by Django 4.1.7 on 2023-04-26 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watercanapp', '0019_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='total_stock',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
