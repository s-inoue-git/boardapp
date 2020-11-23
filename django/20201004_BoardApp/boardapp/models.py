from django.db import models

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    images = models.ImageField(upload_to='')
    good = models.IntegerField(null=True, blank=True, default=0)



