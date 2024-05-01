from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView 
from pages import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.home),
    path("about/", views.about),
    path("work/", views.work),
    path("contact/", views.contact),  
    path("", RedirectView.as_view(url="home/", permanent=True)),
]