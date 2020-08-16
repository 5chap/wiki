from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:TITLE>", views.contents, name="context"),
    path("/new_page", views.new_page, name="new"),
    path("/newEntry", views.newEntry, name="newEntry")
]
