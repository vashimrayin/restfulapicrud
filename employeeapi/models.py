import email
from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    web = models.CharField(max_length=60)
    age = models.CharField(max_length=25)

# Create / Insert / Add-Post
# Retrive / Fetch - Get
# Update / Edit - put
# Delete / Remove 


