from rest_framework import serializers
from .models import Student

class StudentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'phone_number']

    def validate_name(self,value):
        if not value:
            raise serializers.ValidationError("Name should be logical")

    def validate_phone_number(self,value):
        print("in validate")
        if len(str(value)) != 10:
            raise serializers.ValidationError("Phone number should be 10 number long")

    def create(self, validated_data):
        return Student.objects.create(**validated_data)


