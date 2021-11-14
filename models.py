from django.db import models


class Triplog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=600)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

