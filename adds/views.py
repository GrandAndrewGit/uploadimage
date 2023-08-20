from django.shortcuts import render
# from .models import Advert, AdvertImagesList
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from PIL import Image
from .helpers import resize_image, generate_filenames, save_original_image, process_image
from .models import AdvertImagesList
import json

from django.db import transaction


def upload_form(request):
    return render(request, 'home.html', {})


@login_required
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        try:
            max_size = 5 * 1024 * 1024  # 5 MB in bytes
            images_list_obj = AdvertImagesList.objects.get(id='1')

            if images_list_obj.images_qnty >= 8:
                return JsonResponse({'message': f'Resp 400. You have reached max qnty of images'}, status=400)

            if image.size > max_size:
                return JsonResponse({'message': f'Resp 400. {image.name} file size is too large'}, status=400)
            
            # checking by Pillow if image is really image
            img = Image.open(image)
            img.verify()

            # checking by Pillow if image has really correct extensions
            allowed_formats = ['JPEG', 'PNG']
            if img.format not in allowed_formats:
                return JsonResponse({'message': f'Resp 400. {image.name} has not allowed extension.'}, status=400)
            
            unique_filename, unique_filename_webp, only_filename = generate_filenames(image.name)

            save_original_image(image, unique_filename)

            img_path = process_image(unique_filename, unique_filename_webp)

            # with transaction.atomic():
            #     existing_images_list = images_list_obj.images_list
            #     existing_images_list[only_filename] = img_path
            #     images_list_obj.images_list = existing_images_list
            #     images_list_obj.images_qnty += 1
            #     images_list_obj.save()

            # THIS DOESN'T WORK PROPERLY
            existing_images_list = images_list_obj.images_list
            existing_images_list[only_filename] = img_path
            images_list_obj.images_list = existing_images_list
            images_list_obj.images_qnty += 1
            images_list_obj.save()
            
            response_data = {
                'status': 200,
                'message': 'image was uploaded',
                'image_url': img_path,
            }
            return JsonResponse(response_data, status=200)
        except:   
            return JsonResponse({'message': f'Resp 400.{image.name} Image was not saved'}, status=400)
        
    return JsonResponse({'message': 'MUST BE 404 page'}, status=404)





