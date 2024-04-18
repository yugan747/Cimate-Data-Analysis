from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student
from rest_framework.views import APIView


class TestingView(GenericAPIView):
    def get(self,request,*args,**kwargs):
        return Response('The endpoint is working correctly',status=status.HTTP_200_OK)
    
class GetStudentView(APIView):
    serializer_class = StudentSerializer
    def get(self,request,*args,**kwargs):
        all_student_data = Student.objects.all()
        serializer = self.serializer_class(all_student_data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post (self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('The student data has been to the table',status=status.HTTP_201_CREATED)

class UpdateStudentView(APIView):
    def get(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')
        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')
        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def delete(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')
        try:
            student = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
