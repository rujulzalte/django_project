from django.db import models

# Create your models here.

class UserLogin(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=10)
    Phone_no = models.IntegerField()
    state = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.username}"

