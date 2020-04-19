# Generated by Django 2.2 on 2020-04-19 16:39

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('topovske', '0003_auto_20200326_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default='Belgrade', max_length=255),
        ),
        migrations.AddField(
            model_name='location',
            name='location',
            field=location_field.models.plain.PlainLocationField(blank=True, max_length=63),
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='images/'),
        ),
    ]