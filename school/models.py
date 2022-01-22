from django.db import models


class Teacher(models.Model):
    STATUS_CHOICES = (
        ("AVAILABLE", "available "),
        ("NOT_AVAILABLE", "not available")
    )
    name = models.CharField(max_length=40, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, unique=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=40,
                              choices=STATUS_CHOICES,
                              default="AVAILABLE")

    def __str__(self):
        return str(self.name)


class Student(models.Model):
    roll_no = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    department = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class ClassRoom(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="teacher"
    )
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="student"
    )

    def __str__(self):
        return f"{self.teacher} is allotted to {self.student}"
