from django.db import models

# Create your models here.
from petstagram.photos.models import Photo

"""Creating the Comment Model
It is time to create the comment model.
The field Comment Text is required:
Comment Text - it should consist of a maximum of 300 characters
An additional field should be created:
Date and Time of Publication - when a comment is created (only), 
the date of publication is automatically generated
One more thing we should keep in mind is that the comment should relate to the photo 
(as in social apps users comment on a specific photo/post, i.e., 
the comment object is always connected to the photo object).

Creating the Like Model
Finally, create the Like model which should connect one photo to one user.
 However, we do not have a user object, so we will just create the model and add the photo relation:
"""


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

