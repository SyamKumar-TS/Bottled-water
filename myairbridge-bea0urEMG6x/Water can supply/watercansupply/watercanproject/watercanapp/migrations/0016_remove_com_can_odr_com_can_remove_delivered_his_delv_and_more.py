# Generated by Django 4.1.7 on 2023-02-28 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watercanapp', '0015_alter_com_can_odr_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='com_can_odr',
            name='com_can',
        ),
        migrations.RemoveField(
            model_name='delivered_his',
            name='delv',
        ),
        migrations.AddField(
            model_name='delivered_his',
            name='no',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
