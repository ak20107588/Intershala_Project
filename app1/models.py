from django.db import models

# Create your models here.

class User(models.Model):
    FirstName=models.CharField(max_length=255)
    LastName=models.CharField(max_length=255)
    ProfilePicture=models.ImageField( upload_to='profile_photo')
    UserName=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    Address=models.CharField(max_length=255)
    UserType=models.CharField( max_length=255)
    Password=models.CharField( max_length=255)
    ConfirmPassword=models.CharField( max_length=255)