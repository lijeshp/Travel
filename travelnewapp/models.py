from django.db import models

# Create your models here.
class place(models.Model):

    name=models.CharField(max_length=100)
    desc=models.TextField()
    img=models.ImageField(upload_to='picturess')
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class blog(models.Model):
    date=models.CharField(max_length=5)
    month=models.CharField(max_length=50)
    img=models.ImageField(upload_to='blog_picturess')
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    desc=models.TextField()
