# Generated by Django 3.1.7 on 2021-05-16 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nong_san', '0004_auto_20210516_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tb_baocao',
            name='hinh',
            field=models.ImageField(upload_to='images/baocao'),
        ),
    ]
