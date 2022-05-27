from django.db import models
# Create your models here.


class User:
    def __init__(self, user_id, password):
        self.user_id  = user_id
        self.password = password


class shop_user(models.Model):
    class Meta:
        db_table = 'shop_user'
    