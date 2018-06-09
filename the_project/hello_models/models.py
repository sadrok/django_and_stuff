from django.db import models


class Topic(models.Model):
    topic_name = models.CharField(max_length=264)

    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=264, unique=True)
    uri = models.URLField(unique=True)

    def __str__(self):
        return f'{self.name} ({self.uri})'


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{str(self.date)} - {self.name.name}"
