from django.test import TestCase
from school.models import Student, Teacher, ClassRoom


class StudentModelTestcase(TestCase):
    '''
    testing all model here
    '''
    @classmethod
    def setUpTestData(cls):
        cls.class_room_obj=ClassRoom.objects.create(teacher=Teacher.objects.create(
                                                   name='teacher one',
                                                   phone_number='8746937747',
                                                   email='duggudilee@gmail.com'),
            student=Student.objects.create(
                roll_no='1670s609012',
                name='student one',
                department='cse')
        )

    def test_student(self):
        student = Student.objects.get(id=1)
        expected_string = student.name
        self.assertEqual(str(student), expected_string)

    def test_teacher(self):
        teacher = Teacher.objects.get(id=1)
        expected_string = teacher.name
        self.assertEqual(str(teacher), expected_string)

    def test_class_room(self):
        student = Student.objects.get(id=1)
        teacher = Teacher.objects.get(id=1)
        class_room = ClassRoom.objects.get(teacher_id=teacher.id,student_id=student.id)
        self.assertEqual(class_room,self.class_room_obj)









