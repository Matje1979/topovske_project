# Generated by Django 3.0.7 on 2020-07-22 13:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topovske', '0015_auto_20200722_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='camphistory',
            name='text_en',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='camphistory',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]