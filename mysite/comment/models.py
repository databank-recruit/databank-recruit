from django.db import models

# Create your models here.


class Comment(models.Model):
    permissionID = 3
    content = models.TextField()
