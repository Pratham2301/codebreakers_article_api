from django.db import models

# Create your models here.

class Articles(models.Model):
    title=models.CharField(max_length=100,unique=True)
    content=models.TextField(max_length=50000)
    author=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Authors(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
