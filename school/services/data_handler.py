from school.models import Student, Teacher, ClassRoom


class DataHandler(object):

    @classmethod
    def get_or_create_student(cls, data):
        student = Student.objects.filter(roll_no=data['roll_no'])
        if not student.exists():
            created = Student.objects.create(
                roll_no=data['roll_no'],
                name=data['name'],
                department=data['department']
            )
            return created
        return student.first()

    @classmethod
    def allocate_class(cls, data):
        teacher = Teacher.objects.get(id=data['teacher'])
        student = Student.objects.get(id=data['student'])
        try:
            if teacher.status == "AVAILABLE":
                data = ClassRoom.objects.create(student_id=student.id, teacher_id=teacher.id)
                teacher.status = "NOT_AVAILABLE"
                teacher.save()
                return data
            else:
                data = {
                    'message': "teacher not available, already allocated with other student"
                }
            return data
        except Exception as e:
            return e

    @classmethod
    def get_or_create_teacher(cls, data):
        teacher = Teacher.objects.filter(phone_number=data['phone_number'])
        if not teacher.exists():
            created = Teacher.objects.create(
                phone_number=data['phone_number'],
                name=data['name'],
                email=data['email']
            )
            return created
        return teacher.first()
