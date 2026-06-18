from django.db import models

# Create your models here.
class InventoryItem(models.Model):
    name = models.CharField()

    quantity = models.IntegerField()


class IssueInventoryItemRequest(models.Model):
    name = models.CharField()
    

