# Generated by Django 2.2 on 2020-04-26 15:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topovske', '0008_current_publiccampaign'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
