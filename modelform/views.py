from django.shortcuts import render
from .serializers import StudentFormSerializer
from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework import status 
from .forms import StudentForm
from .models import Student
# Create your views here.


class StudentView(APIView):

    serializer_class = StudentFormSerializer

    # def get(self, request):
    #     form = StudentForm()
    #     articles = Student.objects.all()
    #     serializer = StudentFormSerializer(articles,many=True)
    #     return Response(serializer.data)
 
    def post(self, request):
        print("Here")
        serializer = StudentFormSerializer(data = request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK) 
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
