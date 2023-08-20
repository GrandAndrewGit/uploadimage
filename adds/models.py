from django.db import models


class Advert(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    

    def __str__(self):
        return self.title
    

class AdvertImagesList(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    advert = models.OneToOneField(Advert, on_delete=models.CASCADE, null=True)
    images_list = models.JSONField(blank=True, null=True)
    images_qnty = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.title
