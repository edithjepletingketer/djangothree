from django.db import models
from teacher.models import Teacher
# Create your models here.
class Course(models.Model):
	name=models.CharField(max_length=50)
	duration_in_months=models.CharField(max_length=50)
	course_number=models.SmallIntegerField()
	description=models.TextField(max_length=50)
	teacher=models.ForeignKey(Teacher,on_delete=models.PROTECT)
	def __str__(self):
		return self.name


