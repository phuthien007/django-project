# Generated by Django 3.2.1 on 2021-05-06 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20210506_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='price_randian',
            field=models.FloatField(default=0),
        ),
    ]