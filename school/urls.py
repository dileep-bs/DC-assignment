from django.urls import path
from school.views import *

urlpatterns = [
    path('add_student/', AddStudent.as_view(), name="student-create"),
    path('add_teacher/', AddTeacher.as_view(), name="teacher-create"),
    path('allocate_class/', AllocaateClass.as_view(), name="allocate-class"),
    path('get_all_teachers/', ViewAllTeachers.as_view(), name="get-all-teachers"),
    path('get_all_students/', ViewAllStudents.as_view(), name="get-all-students"),
    path('get_class/', ViewClassRoom.as_view(), name="get-all-classes"),
]
