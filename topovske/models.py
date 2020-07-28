from django.db import models
from ckeditor.fields import RichTextField
from location_field.models.plain import PlainLocationField
import datetime

# Create your models here.


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Index(models.Model):
    title = models.CharField(max_length=255)
    lead = models.CharField(max_length=255)
    text = RichTextField()
    image = models.ImageField(upload_to='static/images/', blank=True, default=None)
    image_text = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Project(SingletonModel):
    title = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255, null=True)
    text = RichTextField()

    def __str__(self):
        return self.title


class CampHistory(SingletonModel):
    title = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255, default='')
    text = RichTextField()
    text_en = RichTextField(default='')

    def __str__(self):
        return self.title

class Support(SingletonModel):
    title = models.CharField(max_length=255, default='')
    text = RichTextField(null=True, blank=True)
    text_en = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='static/images/', blank=True, default=None)

    def __str__(self):
        return self.title

class Current(SingletonModel):
    title = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255, default='')
    text = RichTextField()
    text_en = RichTextField(default='')

    def __str__(self):
        return self.title


class PublicCampaign(SingletonModel):
    title = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255, default='')
    text = RichTextField(default='')
    text_en = RichTextField(default='')

    def __str__(self):
        return self.title


class Camp(SingletonModel):
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
    description = models.TextField(blank=True, default='')
    city = models.CharField(max_length=255, default='Belgrade')
    location = PlainLocationField(based_fields=['city'], zoom=7, default='44.79688084502436,20.477120876312256')

    def __str__(self):
        return self.title


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
    title = models.CharField(max_length=100, null=True, blank=True)
    source=models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title


class Interview(models.Model):
    title = models.CharField(max_length=255)
    lead = models.CharField(max_length=255)
    text = RichTextField()
    image = models.ImageField(upload_to='static/images/', blank=True, default=None)