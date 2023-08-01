from django.db import models

class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    name =models.CharField(max_length=40)
    email = models.EmailField()
    DOB = models.DateField()
    mobile = models.IntegerField()
