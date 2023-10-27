from django.db import models

# Create your models here.

class Feature(models.Model):
    name = models.TextField(max_length=2000)

class Context(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    

class Conversation(models.Model):
    content = models.TextField(max_length=200000)
    role = models.CharField(max_length=200) 
    time_stamp = models.DateTimeField(auto_now_add=True)