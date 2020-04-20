from django.db import models
from ckeditor.fields import RichTextField
from location_field.models.plain import PlainLocationField

# Create your models here.


class Index(models.Model):
    title = models.CharField(max_length=255)
    lead = models.CharField(max_length=255)
    text = RichTextField()
    image = models.ImageField(upload_to='static/images/', blank=True, default=None)
    image_text = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()

    def __str__(self):
        return self.title


class Camp(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()

    def __str__(self):
        return self.title


class Archive(models.Model):
    CATEGORIES = [
        ('0', 'Pisma'),
        ('1', 'Spisak Žrtava'),
        ('2', 'Svedočenja'),
        ('3', 'Dokumenti'),
        ('4', 'Fotografije'),
    ]

    title = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/images/', blank=True, default=None)
    category = models.CharField(
        max_length=2,
        choices=CATEGORIES,
        default='0',
    )

    def __str__(self):
        return self.title


class Location(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=255, default='Belgrade')
    location = PlainLocationField(based_fields=['city'], zoom=7, default='44.79688084502436,20.477120876312256')


class Victim(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=255, blank=True, default=None)
    source = models.CharField(max_length=255, blank=True, default=None)

    def __str__(self):
        return ' '.join([self.name, self.surname])


class Photo(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Video(models.Model):
    pass


class Interview(models.Model):
    title = models.CharField(max_length=255)
    lead = models.CharField(max_length=255)
    text = RichTextField()
    image = models.ImageField(upload_to='static/images/', blank=True, default=None)