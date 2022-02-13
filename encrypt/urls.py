from django.urls  import path 
from .views import EncryptedTextCrud

urlpatterns = [
    path("register/", EncryptedTextCrud.as_view(), name="encrypted_path")

]