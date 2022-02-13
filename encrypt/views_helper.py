import hashlib
import hmac 
from .models import EncryptText

def encrypt_text(message):
    key = "7437234273427"
    hmac_obj = hmac.new(key = key.encode(), msg=message.encode(), digestmod=hashlib.sha256)

    return hmac_obj.hexdigest()

def check_availability(password):
        et = EncryptText.objects.filter(
            password = password
        
        )
        if et:
            raise Exception("Already Exist one")