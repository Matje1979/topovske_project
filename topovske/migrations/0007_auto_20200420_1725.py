# Generated by Django 2.2 on 2020-04-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topovske', '0006_location_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='description_sr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='title',
            field=models.CharField(default='title', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='title_sr',
            field=models.CharField(max_length=255, null=True),
        ),
    ]