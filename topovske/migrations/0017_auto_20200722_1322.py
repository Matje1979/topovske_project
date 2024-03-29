# Generated by Django 3.0.7 on 2020-07-22 13:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topovske', '0016_auto_20200722_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='current',
            name='title_en',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='publiccampaign',
            name='title_en',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='current',
            name='text',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='publiccampaign',
            name='text',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
