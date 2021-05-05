from django.db import models

# Create your models here.
class Trainer_Signup(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return self.name