from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import EncryptText

class EncryptedFieldSerializer(ModelSerializer):

    class Meta:
        model = EncryptText
        fields = '__all__'