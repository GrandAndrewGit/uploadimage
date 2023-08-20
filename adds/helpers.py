from PIL import Image
import uuid
import os
import time
from django.conf import settings


def resize_image(img, max_width=800):
    width, height = img.size
    
    if width > max_width:
        new_height = int((max_width / width) * height)
        resized_img = img.resize((max_width, new_height), Image.LANCZOS)
        return resized_img
    else:
        return img
    

def generate_filenames(file_name):
    current_time_seconds = int(time.time())
    unique_uuid = str(current_time_seconds) + uuid.uuid4().hex[:9]
    _, image_extension = os.path.splitext(file_name)
    filename_jpg = f"{unique_uuid}{image_extension}"
    filename_webp = f"{unique_uuid}.webp"
    return [filename_jpg, filename_webp, unique_uuid]


def save_original_image(image, file_name):
    with open(f"media/uploads/{file_name}", "wb") as f:
        for chunk in image.chunks():
            f.write(chunk)


def process_image(unique_filename, unique_filename_webp):
    image_url = os.path.join(settings.MEDIA_ROOT, 'uploads', unique_filename)
    img_openned_with_pillow = Image.open(image_url)
    img_path = os.path.join(settings.MEDIA_ROOT, 'uploads', unique_filename_webp)
    resized_image = resize_image(img_openned_with_pillow)
    img_path_for_front = os.path.join(settings.MEDIA_URL, 'uploads', unique_filename_webp)
    resized_image.save(img_path, 'webp', optimize=True, quality=70)
    os.remove(image_url)
    return img_path_for_front