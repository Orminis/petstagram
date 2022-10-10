from django.shortcuts import render


# accounts\views.py

# Create your views here.

def register_user(request):
    return render(request, template_name="accounts/register-page.html")


def login_user(request):
    return render(request, template_name="accounts/login-page.html")


def show_profile(request, pk: int):
    return render(request, template_name="accounts/profile-details-page.html")


def edit_profile(request, pk: int):
    return render(request, template_name="accounts/profile-edit-page.html")


def delete_profile(request, pk: int):
    return render(request, template_name="accounts/profile-delete-page.html")
