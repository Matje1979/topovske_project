# Generated by Django 3.0.7 on 2020-07-24 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topovske', '0020_auto_20200724_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
