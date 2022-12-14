# photos\urls.py
from django.urls import path, include

from petstagram.photos import views

urlpatterns = (
    path("add/", views.add_photo, name="add-photo"),
    path("<int:pk>/",
         include([
             path("", views.photo_details, name="details-photo"),
             path("edit/", views.photo_edit, name="edit-photo"),
         ]))
)
