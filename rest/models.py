from django.db import models


class Info(models.Model):
    # id = models.IntegerField()
    checked = models.BooleanField()
    name = models.CharField(max_length=20)
    Type = models.CharField(max_length=100)
    Age = models.IntegerField()
    Description = models.TextField(max_length=200)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    