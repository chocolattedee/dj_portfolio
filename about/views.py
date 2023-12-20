from django.shortcuts import render
from .models import About

# Create your views here.
def home(request):
    content = About.objects.all()
    context = {'images':content}
    return render(request, "about/about_index.html", context)    