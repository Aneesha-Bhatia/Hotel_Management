from django.db import models

# Create your models here.

class Manager(models.Model):
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    age = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True, blank=True)
    contactno = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='manager/photo/', null=True, blank=True)



room_list = [
    ('AC','AC'),
    ('NON-AC','NON-AC'),
    ('DELUXE','DELUXE'),
    ('KING','KING'),
    ('QUEEN','QUEEN')
    ]

class Room(models.Model):
    room_type = models.CharField(choices=room_list, max_length=40)
    price = models.IntegerField(null=True,blank=True)
    capacity = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='photo/', null=True, blank=True)
    contactno = models.IntegerField(default=0)