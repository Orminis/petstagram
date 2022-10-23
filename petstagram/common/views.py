from django.shortcuts import render, redirect

# common\views.py

# Create your views here.
from petstagram.common.models import PhotoLike
from petstagram.photos.models import Photo


# TODO: !!!Докато нямам users така ... после го оправяме!!! when authentication is available!!!
def apply_likes_photo(photo):
    photo.likes_count = photo.photolike_set.count()
    return photo


def apply_user_liked_photo(photo):
    photo.is_liked_by_user = photo.likes_count > 0
    return photo


def common(request):
    photos = [apply_likes_photo(photo) for photo in Photo.objects.all()]
    photos = [apply_user_liked_photo(photo) for photo in photos]
    context = {
        "photos": photos
    }
    return render(request, "common/home-page.html", context)


def get_user_liked_photo(photo_id):
    # TODO: when auth
    return PhotoLike.objects.filter(photo_id=photo_id)


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
    redirected_path = request.META['HTTP_REFERER'] + f'#photo-{photo_id}'
    return redirect(redirected_path)


