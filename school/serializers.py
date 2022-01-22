from rest_framework import serializers

from .models import Student, Teacher, ClassRoom


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('roll_no', 'name', 'department')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('name', 'phone_number', 'email', 'status')


class AllocateClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'
