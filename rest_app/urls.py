from django.urls import path
from .views import get_hello_world

urlpatterns = [
    path("hello-world/", get_hello_world, name='get_hello_world')
]