from django.db import models
from datetime import datetime
# Create your models here.
# Create your models here.
from django.contrib.auth.models import AbstractUser
class customuser(AbstractUser):
    pass
    email = models.CharField(max_length=1000);
    delete_date = models.DateField(default=datetime.now());
class airlines(models.Model):
    name = models.CharField(max_length=1000);
    type = models.CharField(max_length=1000);
    def __str__(self):
        return self.name;
class author(models.Model):
    name = models.CharField(max_length=400);
    address = models.CharField(max_length=1000);
    def __str__(self):
        return  self.name;
class cookbook(models.Model):
    name = models.CharField(max_length=200);
    author = models.ForeignKey(author, related_name='author', on_delete=models.CASCADE);
    def __str__(self):
        return self.name;
class duplicate(models.Model):
    name = models.CharField(max_length=200);
    def __str__(self):
        return self.name;