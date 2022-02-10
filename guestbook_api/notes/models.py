from django.db import models

# Create your models here.

"""
class Note
    title str
    content str
    date_created datetime
"""

class Note(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title