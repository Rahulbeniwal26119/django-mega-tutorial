from django.urls import path
from .views import print_query

urlpatterns = [
    path("loan/<int:pk>", print_query, name="Print Query")
]