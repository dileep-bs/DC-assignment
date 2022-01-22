from django.test import TestCase

from school.models import Student, Teacher


# Create your tests here.
class ViewAllStudentsTest(TestCase):
    '''
    testing all views here
    '''
    @classmethod
    def setupStudentTestData(cls):
        num_of_students = 5
        for student in range(num_of_students):
            Student.objects.create(roll_no='123456' + student, name='test' + student, department='cse')

    @classmethod
    def setupTeachersTestData(cls):
        num_of_teachers = 5
        for teacher in range(num_of_teachers):
            Teacher.objects.create(name='sample' + teacher, phone_number='123456' + teacher, email="sample@gmail.com",
                                   status='available')

    def test_get_all_student(self):
        response = self.client.get('/school/get_all_students/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_teachers(self):
        res = self.client.get('/school/get_all_teachers/')
        self.assertEqual(res.status_code, 200)

    def test_post_students(self):
        num_of_students = 5
        for student in range(num_of_students):
            Student.objects.create(roll_no='123456', name='test', department='cse')

    def test_post_teachers(self):
        num_of_teachers = 5
        for teacher in range(num_of_teachers):
            Teacher.objects.create(name='sample', phone_number='123456'+str(teacher), email="sample@gmail.com",
                                   status='available')

    def test_get_teachers(self):
        num_of_teachers = 5
        for teacher in range(num_of_teachers):
            Teacher.objects.create(name='sample', phone_number='123456' + str(teacher), email="sample@gmail.com",
                                   status='available')
        data=Teacher.objects.all()
        self.assertEqual(data.first().name, 'sample')





