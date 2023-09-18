from django.db import models
import uuid


class Dept(models.Model):
    depi_id = models.CharField(primary_key='True', max_length=255)
    name = models.CharField(max_length=255)

class student(models.Model):
    student_id = models.CharField(primary_key='True', max_length=255, default=None)
    name = models.CharField(max_length=255, default=None)
    rollnumber = models.CharField(max_length=255, default=None)
    branch = models.CharField(max_length=255, default=None)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)


# Many - Many
class People(models.Model):
    name = models.CharField(max_length=255, default=None)
    courses = models.ManyToManyField('Course')

class Course(models.Model):
    title = models.CharField(max_length=255, default=None)