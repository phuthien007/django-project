# Generated by Django 3.2.1 on 2021-05-09 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_alter_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateField(default=datetime.date(2021, 5, 9)),
        ),
    ]
