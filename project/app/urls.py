from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name = "index"),
    path("prompt/", views.prompt, name = "prompt")
    ]