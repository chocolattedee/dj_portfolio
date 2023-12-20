from django.urls import path, include
from about import views

urlpatterns = [
    path("", views.home, name='about'),
    # path('', include('pages.urls')),
    # path('', include('projects.urls')),

]
