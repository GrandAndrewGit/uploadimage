from django.contrib import admin
from .models import Advert, AdvertImagesList


class AdvertAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    
admin.site.register(Advert, AdvertAdmin)



class AdvertImagesListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'images_qnty']
    list_display_links = ['id', 'title']
    
admin.site.register(AdvertImagesList, AdvertImagesListAdmin)