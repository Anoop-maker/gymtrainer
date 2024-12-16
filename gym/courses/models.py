from django.db import models

# Create your models here.
class Trainer(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to="trainer")

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    image = models.ImageField(upload_to="trainer")
    count=models.IntegerField()
    waiting_time=models.IntegerField()
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
