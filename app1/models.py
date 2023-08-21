from django.db import models

# Create your models here.

class User(models.Model):
    FirstName=models.CharField(max_length=255)
    LastName=models.CharField(max_length=255)
    ProfilePicture=models.FileField( upload_to='profilepicture')
    UserName=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    Address=models.CharField(max_length=255)
    UserType=models.CharField( max_length=255)
    Password=models.CharField( max_length=255)
    ConfirmPassword=models.CharField( max_length=255)

class Blog(models.Model):
    Title=models.CharField(max_length=250)
    BlogImages=models.FileField( upload_to='profilepicture')
    Category=models.CharField( max_length=250)
    Summary=models.CharField( max_length=1000)
    Content=models.CharField(max_length=1000)
    IsDraft= models.BooleanField(default=False)

