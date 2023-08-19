from django.db import models


class Advert(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.title
    

class AdvertImagesList(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.title
