from PIL import Image
from io import BytesIO
from uuid import uuid4
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile


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


def column_calc(i: int) -> int:
    if i % 2 == 0:
        if i % 4 == 0:
            return 4
    return 3


def calc(i: int, column: int = 3) -> tuple:
    if column == 3:
        x = int(i / 3)
        y = i - x
        return x, y
    else:
        x = int(i / 4)
        z = i - x
        y = z - x
        return x, y, z


def create_image_column(l: list) -> list:
    ll = len(l)
    print(l, ll)
    if ll < 6:
        return [l]
    elif 6 <= ll < 19:
        match ll:
            case 6:
                x, y = calc(ll, 3)
                return [l[:x], l[x:y], l[y:]]
            case 9:
                x, y = calc(ll, 3)
                return [l[:x], l[x:y], l[y:]]
            case 12:
                x, y = calc(ll, 3)
                return [l[:x], l[x:y], l[y:]]
            case 15:
                x, y = calc(ll, 3)
                return [l[:x], l[x:y], l[y:]]
            case 18:
                x, y = calc(ll, 3)
                return [l[:x], l[x:y], l[y:]]
    elif ll >= 19:
        match column_calc(ll):
            case 4:
                x, y, z = calc(ll, 4)
                return [l[:x], l[x:y], l[y:z], l[z:]]
            case 3:
                x, y = calc(ll, 3)
                return [l[:x], l[x:y], l[y:]]
