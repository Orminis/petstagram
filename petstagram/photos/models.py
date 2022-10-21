from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from petstagram.pets.models import Pet


def validate_image_less_than_5mgb(image):
    filesize = image.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit * (1024**2):
        raise ValidationError(f"Max file size is 5MBs")


class Photo(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    # Requires mediafiles to work correctly
    photo = models.ImageField(
        upload_to='mediafiles/pet_photo/',
        validators=(validate_image_less_than_5mgb,),
        null=False,
        blank=True,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            # Django/python validation not DV Validation
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
