from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData["title"]) < 5:
            errors["title"] = "Show's title should be at least 5 characters."
        if len(postData["network"]) < 3:
            errors["network"] = "Show's network should be at least 3 characters."
        if len(postData["desc"])>=1:
            if len(postData["desc"]) < 10:
                errors["desc"] = "If description exits, it should be at least 10 characters."
        release_date = datetime.strptime(postData["release_date"], '%Y-%m-%d')
        recent_date = datetime.now()
        if release_date > recent_date:
            errors["release_date"] = "Release date should be in the past"
        return errors
# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length = 255)
    desc = models.TextField(null=True)
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
