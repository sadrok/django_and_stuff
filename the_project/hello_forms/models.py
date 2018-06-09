from django.db import models

class SiteUser(models.Model):

    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField()
    website = models.URLField(blank=True)
    note = models.TextField(blank=True)
