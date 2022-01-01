from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    username = models.CharField(max_length=70,default=None)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)
    cpassword = models.CharField(max_length=70)
    address = models.CharField(max_length=270,null=False, blank=False, default=None)
