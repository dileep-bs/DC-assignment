# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Teacher, Student, ClassRoom
from .serializers import StudentSerializer, TeacherSerializer, AllocateClassRoomSerializer
from .services.data_handler import DataHandler


class AddStudent(generics.CreateAPIView):
    """Adding student into database"""
    serializer_class = StudentSerializer

    def post(self, request):
        stud = self.serializer_class(data=request.data)
        if stud.is_valid():
            student = DataHandler.get_or_create_student(stud.data)
            response = {
                "message": "student data added successfully",
                'data': self.serializer_class(student).data
            }
            return Response(response)
        return Response({"message": "check request body"})


class AllocaateClass(generics.CreateAPIView):
    """Allocate student into classroom (ex: student_pk and teacher_pk)"""
    serializer_class = AllocateClassRoomSerializer

    def post(self, request):
        class_data = self.serializer_class(data=request.data)
        print("aaaaaa", request.data['teacher'])
        print("aaaaaa", request.data['student'])
        print(class_data)
        if class_data.is_valid():
            data = DataHandler.allocate_class(class_data.data)
            response = {
                "data": self.serializer_class(data).data
            }
            return Response(response)
        return Response({"message": "check request body"})


class ViewAllTeachers(APIView):
    """List of all teachers"""
    serializer_class = TeacherSerializer

    def get(self, request):
        data = Teacher.objects.all()
        all_teachers = self.serializer_class(data, many=True).data
        response = {
            "data": all_teachers
        }
        return Response(response)


class AddTeacher(generics.CreateAPIView):
    """Adding teacher into database"""
    serializer_class = TeacherSerializer

    def post(self, request):
        teacher = self.serializer_class(data=request.data)
        if teacher.is_valid():
            teacher = DataHandler.get_or_create_teacher(teacher.data)
            response = {
                "message": "teacher data added successfully",
                'data': self.serializer_class(teacher).data
            }
            return Response(response)
        return Response({"message": "check request body"})


class ViewAllStudents(APIView):
    """List of all students"""
    serializer_class = StudentSerializer

    def get(self, request):
        data = Student.objects.all()
        all_students = self.serializer_class(data, many=True).data
        response = {
            "data": all_students
        }
        return Response(response)


class ViewClassRoom(APIView):
    """List of all classroom which is allocated"""
    serializer_class = AllocateClassRoomSerializer

    def get(self, request):
        data = ClassRoom.objects.all()
        all_class = self.serializer_class(data, many=True).data
        response = {
            "data": all_class
        }
        return Response(response)
