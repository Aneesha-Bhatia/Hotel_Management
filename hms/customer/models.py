from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    age = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True, blank=True)
    contactno = models.IntegerField(default=0)
    coming_from = models.CharField(max_length=20, default="")
    going_to = models.CharField(max_length=20, default="")
    photo = models.ImageField(upload_to='manager/photo/', null=True, blank=True)


