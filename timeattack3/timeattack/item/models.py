from operator import mod
from turtle import ondrag
from django.db import models
from user.models import shop_user
# Create your models here.

class Item(models.Model):
    class Meta:
        db_table = 'item'
    owner = models.ForeignKey(shop_user, on_delete=models.CASCADE)
    product = models.CharField(max_length=30)
    desc = models.CharField(max_length=200)
    price = models.IntegerField()

class Status_delivery(models.Model):
    class Meta:
        db_table = 'item-del-status'
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    