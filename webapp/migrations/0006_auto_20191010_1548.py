# Generated by Django 2.2.3 on 2019-10-10 10:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20191009_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='delete_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 10, 15, 48, 19, 626644)),
        ),
    ]
