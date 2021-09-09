from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name
