# pets\urls.py

from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path("add/", views.add_pet, name="add-pet"),
    path("<str:username>/pet/<slug:pet_name>/",
         include([
             path("", views.show_pet_details, name="details-pet"),
             path("edit/", views.edit_pet, name="edit-pet"),
             path("delete/", views.delete_pet, name="delete-pet"),
         ])),
]
