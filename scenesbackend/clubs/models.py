from django.db import models


class Club(models.Model):
    name = models.CharField()
    description = models.CharField()


class Notification(models.Model):
    title = models.CharField()
    body = models.CharField()
    
