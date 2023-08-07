from django.db import models

# Create your models here.
class todo_model(models.Model):
    task=models.CharField(max_length=250)
    

    def __str__(self):
        return self.task