from django.shortcuts import render


# common\views.py

# Create your views here.

def common(request):
    return render(request, "common/home-page.html")
