# commons\urls.py

from django.urls import path

from petstagram.common import views

urlpatterns = [
    path("", views.common, name='home'),
]
