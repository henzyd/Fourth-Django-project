# Generated by Django 4.1.1 on 2022-09-13 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 13, 12, 51, 0, 895874)),
        ),
    ]
