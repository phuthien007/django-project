# Generated by Django 3.2.1 on 2021-05-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_alter_comments_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(default='good', max_length=1000),
        ),
    ]