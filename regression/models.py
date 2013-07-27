from django.db import models
from django import forms
# Create your models here.
class Regression(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.CharField(max_length = 500, blank = True, null = True)
    data = forms.FileField()
    
    def __unicode__(self):
        return self.id
    