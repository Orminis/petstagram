from django.db import models

# Create your models here.
from petstagram.photos.models import Photo


class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False
    )
    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )
    # One-to-many relation to Photo model (id/pk)
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )


class PhotoLike(models.Model):
    # Photo's field for likes is named - `{NAME_OF_THIS_MODEL.lower()}_set` !!!
    # TODO: Check this again at video: 02:15:15
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

    # # when we have users
    # user = models.ForeignKey(
    #     User
    # )

