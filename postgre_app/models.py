from django.db import models

class Dept(models.Model):
    depi_id = models.CharField(primary_key='True', max_length=255)
    name = models.CharField(max_length=255)