# commons\urls.py

from django.urls import path

from petstagram.common import views

urlpatterns = [
    path("", views.common, name='home'),
    path("like/<int:photo_id>", views.like_photo, name="like-photo"),
    path("share/<int:photo_id>", views.share_photo, name="share-photo"),
]
