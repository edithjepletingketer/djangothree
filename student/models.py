from django.db import models
from course.models import Course
import datetime
from django.core.exceptions import ValidationError
# Create your models here.
class Students(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    registration_number=models.CharField(max_length=50)
    place_of_residence=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    guardian_no=models.CharField(max_length=50)
    id_no=models.IntegerField()
    date_joined=models.DateField()
    courses=models.ManyToManyField(Course, blank = True, related_name="Students", null = True)
    profile_picture=models.ImageField(upload_to="profiles",blank=True,null = True)
    def __str__(self):
        return self.first_name+" "+self.last_name

    def full_name(self):
        return "{} {}".format(
            self.first_name,
            self.last_name
            )

    



