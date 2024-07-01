from django.db import models

class task(models.Model):

    todo = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.todo   

# Create your models here.
