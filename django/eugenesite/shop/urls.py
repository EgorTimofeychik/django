from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_blog),
    path("article1", views.my_blog1),
    path("article2", views.my_blog2),
]