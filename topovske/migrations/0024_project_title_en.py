# Generated by Django 3.0.7 on 2020-07-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topovske', '0023_auto_20200724_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
