# Generated by Django 3.2.1 on 2021-05-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_alter_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(default='good', max_length=200),
        ),
    ]
