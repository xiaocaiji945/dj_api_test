import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.create_at >= timezone.now() - datetime.timedelta(days=1)

class Ttttt(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=True, null=True)
    votes = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

