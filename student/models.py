from django.db import models
from course.models import Course

# Create your models here.
class Students(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	date_of_birth=models.DateField()
	registeration_number=models.CharField(max_length=50)
	place_of_residence=models.CharField(max_length=50)
	phone_number=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	guardian_no=models.CharField(max_length=50)
	id_no=models.IntegerField()
	date_joined=models.DateField()
	courses=models.ManyToManyField(Course)
	profile_picture=models.ImageField(upload_to="profiles",blank="True")
	def __str__(self):
		return self.first_name+" "+self.last_name	


