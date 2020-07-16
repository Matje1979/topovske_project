# Generated by Django 2.2 on 2020-03-14 14:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, default=None, upload_to='static/images/')),
                ('category', models.CharField(choices=[('0', 'Pisma'), ('1', 'Spisak Žrtava'), ('2', 'Svedočenja'), ('3', 'Dokumenti'), ('4', 'Fotografije')], default='0', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('lead', models.CharField(max_length=255)),
                ('text', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, default=None, upload_to='static/images/')),
                ('image_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('lead', models.CharField(max_length=255)),
                ('text', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, default=None, upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]