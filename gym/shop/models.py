from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=20)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.EmailField(max_length=20,unique=True)
    password = models.IntegerField()
    conformpassword = models.IntegerField()

    def __str__(self):
        return self.username