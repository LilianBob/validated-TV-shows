from django.db import models
from datetime import datetime


# Create your models here.
class ShowManager(models.Manager):
    def validate(self, fieldData):
        errors = {}
        if len(fieldData['title']) < 2:
            errors['title'] = 'Title field should be at least 2 characters'
        if len(fieldData['network']) < 2:
            errors['network'] = 'Network field should be at least 2 characters'
        if fieldData['description'] != '' and len(fieldData['description']) < 8:
            errors['description'] = 'Description should be at least 8 characters'
        if datetime.strptime(fieldData['release_date'], '%Y-%m-%d') > datetime.now():
            errors['release_date'] = 'Release Date should be in the past'
        return errors
class Show(models.Model):
    title= models.CharField(max_length=255)
    network= models.CharField(max_length=255)
    release_date= models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    description= models.TextField(null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    objects=ShowManager()

