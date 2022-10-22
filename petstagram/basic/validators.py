from django.core.exceptions import ValidationError


def megabytes_to_bytes(mbs):
    return mbs * 1024 * 1024


def validate_image_less_than_5mgb(image):
    filesize = image.file.size
    megabyte_limit = 5.0
    if filesize > megabytes_to_bytes(megabyte_limit):
        raise ValidationError(f"Max file size is 5MBs")