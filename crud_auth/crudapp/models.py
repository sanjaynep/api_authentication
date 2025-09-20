
from django.db import models

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
         return self.name
# Create your models here.
