from django.contrib import admin

# Register your models here.
from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'description',
                    'publication_date',
                    'pets',
                    )

    @staticmethod
    def pets(photo_obj):
        # PhotoAdmin inherits Photo, so it has tagged_pets too
        # pets returns queryset of pet/s tagged to the picture
        tagged_pets = photo_obj.tagged_pets.all()
        if tagged_pets:
            return ', '.join(obj.name for obj in tagged_pets)
        return "No Pets!"
