from django.contrib import admin
from hello_models import models

# Register your models here.
admin.site.register([models.Topic, models.Webpage, models.AccessRecord])