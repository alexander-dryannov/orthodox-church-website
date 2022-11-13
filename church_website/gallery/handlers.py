from io import BytesIO
from uuid import uuid4

from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image


def get_new_size(size: int) -> int:
    if size >= 600:
        return int(round(size / 1000))
    else:
        return 1


def converter(image=None, fmt=settings.CONVERTING_SAVED_IMAGE):
    rgb_image = Image.open(image).convert('RGB')
    # exif = rgb_image.getexif()
    origin_width, origin_height = rgb_image.size
    width = get_new_size(origin_width)
    height = get_new_size(origin_height)
    binary_image = BytesIO()
    rgb_image.save(binary_image, fmt)
    # rgb_image.save(binary_image, fmt, exif=exif)
    image_name = f'{uuid4().hex}.{fmt}'
    binary_image.seek(0)
    return InMemoryUploadedFile(
        file=binary_image,
        field_name='ImageField',
        name=image_name,
        content_type=f'image/{fmt}',
        size=rgb_image.size,
        charset=None
    ), width, height, origin_width, origin_height


# Для организации колонок
def create_image_column(images: list) -> list:
    columns = [[], [], [], []]
    size_data = {'width': [], 'height': []}
    # Stage 1
    for image in images:
        if image.origin_width > image.origin_height:
            size_data['width'].append(image)
        else:
            size_data['height'].append(image)
    # Stage 2
    try:
        while True:
            if len(size_data['height']) != 0:
                for column in columns:
                    image = size_data['height'].pop(-1)
                    column.append(image)
            else:
                break
    except IndexError:
        pass

    for column in columns[1:]:
        if len(column) < len(columns[0]):
            for _ in range(2):
                column.append(size_data['width'].pop(-1))
    # Stage 3
    try:
        while True:
            if len(size_data['width']) != 0:
                for column in columns:
                    image = size_data['width'].pop(-1)
                    column.append(image)
            else:
                break
    except IndexError:
        pass
    return columns
