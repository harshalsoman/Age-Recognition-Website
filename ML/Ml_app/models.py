from django.db import models

# Create your models here.
class Image(models.Model):
    pic = models.ImageField(upload_to="myimage")
    #date= models.DateField(auto_now_add=True)