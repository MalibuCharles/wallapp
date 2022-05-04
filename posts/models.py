from email.mime import image
from django.db import models

# Create your models here.
# id= models.AutoField(primary_key=True)
class Post(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)