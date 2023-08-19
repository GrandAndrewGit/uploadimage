from django.urls import path
from . import views 

app_name = 'adds'

urlpatterns = [
    path('', views.upload_form, name='upload-form'),
    path('upload-image', views.upload_image, name='upload-image'),
]