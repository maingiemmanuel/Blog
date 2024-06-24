from django.db import models


class Blogs(models.Model):
    Title = models.CharField(max_length=20)
    Content = models.CharField(max_length=30)
    Publication_Date = models.DateField()
