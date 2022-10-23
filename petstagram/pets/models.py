from django.db import models
from django.utils.text import slugify
from petstagram.basic.model_mixins import StrFromFieldsMixin

# Create your models here.


class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')

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
        null=True,
        blank=True,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    # create unique slug and saves it automatically
    def save(self, *args, **kwargs):
        # Create/Update object from instance Pet
        super().save(*args, **kwargs)
        # If there is not created slug it creates a new one and updates the pet object
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')
        """
        Without the `if` the following scenario might happen:
        the url is `/pets/1-alba` and at later stage pet name is changed to albata 
        the new url will be `/pets/1-albata`, but `/pets/1-alba` will not work.
        """

        # Update /  enters into built-in function save and continues saving the info in the DB
        return super().save(*args, **kwargs)

    # def __str__(self):
    #     return f'ID = {self.id}; Name = {self.name}'
