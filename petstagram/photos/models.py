from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.basic.model_mixins import StrFromFieldsMixin
from petstagram.basic.validators import validate_image_less_than_5mgb
from petstagram.pets.models import Pet


# Create your models here.


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('photo', 'location')

    MEDIA_FILES = 'mediafiles/pet_photo/'
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    # Requires mediafiles to work correctly
    photo = models.ImageField(
        upload_to=MEDIA_FILES,
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
