from django.db import models

# Create your models here.
class Users(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=60)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=16)
    c_password=models.CharField(max_length=16)
    
    def __str__(self):
        return self.username