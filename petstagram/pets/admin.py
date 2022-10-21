from django.contrib import admin

# Register your models here.
from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
