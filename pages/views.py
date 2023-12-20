import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
from pages.models import Home
# Create your views here.
def home_index(request):
    img_list = Home.objects.all()
    context = {'images' : img_list}
    return render(request, "pages/home_index.html", context)