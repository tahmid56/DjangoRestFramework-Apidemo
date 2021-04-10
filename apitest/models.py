from django.db import models

# Create your models here.
class Items(models.Model):
    itemId = models.IntegerField()
    itemName = models.CharField(max_length=50)
    itemCategory = models.CharField(max_length=10)
    itemPrice = models.FloatField()

    def __str__(self):
        return self.itemName
    