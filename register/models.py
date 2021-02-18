from django.db import models


# Create your models here.


class Designation(models.Model):
    tittle = models.CharField(max_length=100)

    def __str__(self):
        return self.tittle


class Employee(models.Model):
    fullname = models.CharField(max_length=200)
    emp_code = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)
