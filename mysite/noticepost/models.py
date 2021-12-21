from django.db import models

# Create your models here.


class NoticePost(models.Model):
    permissionID = 2
    title = models.CharField(max_length=100)
    content = models.TextField()
