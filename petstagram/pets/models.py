from django.db import models

# Create your models here.


class Pet(models.Model):
    MAX_NAME = 30
    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
    )
    personal_photo = models.URLField(
        null=False,
        blank=False,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=False,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
