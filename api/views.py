from django.shortcuts import render
from student.models import Students
from teacher.models import Teacher
from course.models import Course

from .serializers import StudentsSerializer
from .serializers import TeacherSerializer
from .serializers import CourseSerializer

from rest_framework import viewsets




class StudentViewSet(viewsets.ModelViewSet):
	queryset=Students.objects.all()
	serializer_class=StudentsSerializer

class TeacherViewSet(viewsets.ModelViewSet):
	queryset=Teacher.objects.all()
	serializer_class=TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
	queryset=Course.objects.all()
	serializer_class=CourseSerializer

# Create your views here.
