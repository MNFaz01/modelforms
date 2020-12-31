from django.db import models

# Create your models here.
class Projects(models.Model):
    startDate=models.DateField()
    endDate=models.DateField()
    name=models.CharField(max_length=20)
    assignedTo=models.CharField(max_length=10)
    priority=models.IntegerField()
