from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class StudentSerializerTestCase(APITestCase):
    '''
    testing all apis here
    '''

    def test_student_creation(self):
        payload = {
            "roll_no": "1670s609012",
            "name": "student one",
            "department": "cse"
        }
        response = self.client.post(reverse("student-create"), payload)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_teacher_creation(self):
        payload = {
            "name": "teacher one",
            "phone_number": "8746937747",
            "email": "duggudilee@gmail.com"
        }
        response = self.client.post(reverse("teacher-create"), payload)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_allocate_class(self):
        payload = {
            "teacher": "3",
            "student": "12"
        }
        response = self.client.post(reverse("allocate-class"), payload)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_all_teachers(self):
        response={
                    "data": [
                        {
                            "name": "teacher one",
                            "phone_number": "8746937747",
                            "email": "duggudilee@gmail.com",
                            "status": "NOT_AVAILABLE"
                        }
                    ]
                }
        print("before",response)
        response = self.client.get(reverse("get-all-teachers"), response)
        print("after",response)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_all_students(self):
        response={
                    "data": [
                        {
                            "roll_no": "1670s609012",
                            "name": "student one",
                            "department": "cse"
                        },
                        {
                            "roll_no": "121212",
                            "name": "asasa",
                            "department": "qwqw"
                        }
                    ]
                }
        response = self.client.get(reverse("get-all-teachers"), response)
        self.assertEqual(status.HTTP_200_OK, response.status_code)




