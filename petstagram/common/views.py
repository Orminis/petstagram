import pyperclip
from django.shortcuts import render, redirect
from django.urls import reverse

from petstagram.basic.photo_utils import apply_likes_count, apply_user_liked_photo
from petstagram.common.models import PhotoLike
from petstagram.common.utils import get_user_liked_photo, get_photo_url
from petstagram.photos.models import Photo


# common\views.py

# Create your views here.


def common(request):
    photos = [apply_likes_count(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    context = {
        "photos": photos
    }
    return render(request, "common/home-page.html", context)


def like_photo(request, photo_id):
    user_liked_photos = get_user_liked_photo(photo_id)
    if user_liked_photos:
        user_liked_photos.delete()
    else:
        # Variant 2
        PhotoLike.objects.create(
            photo_id=photo_id,
        )
    # Create
    # # Variant 1
    # photo_like = PhotoLike(
    #     photo_id=photo_id
    # )
    # photo_like.save()

    # # Variant 3 !!! NOT CORRECT!!! Making 1 additional call to the DB
    # # correct ONLY if validation is needed
    # photo = Photo.objects.get(pk=photo_id)
    # PhotoLike.objects.create(
    #     photo=photo,
    # )
    return redirect(get_photo_url(request, photo_id))


def share_photo(request, photo_id):
    photo_details_url = reverse('details-photo', kwargs={'pk': photo_id})

    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, photo_id))
