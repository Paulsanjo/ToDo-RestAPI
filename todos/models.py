from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        """Representation of the To-do Model"""
        return self.title

