from django.db import models


# Create your models here.
class Urls(models.Model):
    original_url = models.CharField(max_length=256)
    hash = models.CharField(max_length=10)
    creation_date = models.DateTimeField('creation date')
    click_remaining = models.IntegerField(default=1)