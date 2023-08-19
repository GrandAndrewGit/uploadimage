from django.shortcuts import render
# from .models import Advert, AdvertImagesList
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import os
# from uploadapp.settings import MEDIA_ROOT
from django.conf import settings
from PIL import Image


def upload_form(request):
    return render(request, 'home.html', {})


# @login_required
# def upload_view(request):
#     if request.method == "POST":
#         image_files = request.FILES.getlist("image")

#         for image_file in image_files:
#             # Process or save the image as needed
#             # Sample code to save the image
#             with open(f"uploads/{image_file.name}", "wb") as f:
#                 for chunk in image_file.chunks():
#                     f.write(chunk)

#         return JsonResponse({"message": "Images uploaded successfully."})

#     return render(request, "index.html")


@login_required
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        max_size = 1 * 1024 * 1024  # 5 MB in bytes
        try:
            if image.size > max_size:
                return JsonResponse({'message': f'Resp 400. {image.name} file size is too large'}, status=400)
            
            # checking by Pillow if image is really image

            img = Image.open(image)
            img.verify()
            print(img)

            # checking by Pillow if image has really correct extensions
            allowed_formats = ['JPEG', 'PNG']
            if img.format not in allowed_formats:
                return JsonResponse({'message': f'Resp 400. {image.name} has not allowed extension.'}, status=400)
            

            with open(f"media/uploads/{image.name}", "wb") as f:
                for chunk in image.chunks():
                    f.write(chunk)
            image_url = os.path.join(settings.MEDIA_ROOT, 'uploads', image.name)
            

            imgOpennedWithPillow = Image.open(image_url)
            img_path = os.path.join(settings.MEDIA_ROOT, 'uploads', 'file.jpg')
            imgOpennedWithPillow.save(img_path)

            
            # img_path = os.path.join(settings.MEDIA_URL, 'uploads', 'file.jpg')
            # f_img_path = '/Users/grand/Documents/3_sandbox/upload-images' + img_path
            # print(f_img_path)
            # print('step 1')
            # try:
            #     img.save(f_img_path)
            # except Exception as e:
            #     print('Exception:', e)

            response_data = {
                'status': 200,
                'message': 'image was uploaded',
                'image_url': 'asa',
            }
            return JsonResponse(response_data, status=200)
        except:   
            return JsonResponse({'message': f'Resp 400.{image.name} Image was not saved'}, status=400)
        
    return JsonResponse({'message': 'MUST BE 404 page'}, status=404)



