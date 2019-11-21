from django.test import TestCase
from .models import Teacher
from .forms import TeacherForm
import datetime


		

class CreateTeacherTestCase(TestCase):

	def setUp(self):
		self.data = {
		"first_name" : "James",
		"last_name" :"Mwai",
		"date_of_birth" : datetime.date(1990,2,8),
		"registration_number" : "09248", 
		"email" : "smatemwa@gmail.com",
		"phone_number": "071163212",
		"place_of_residence": "Kilimani",
		"id_no" : 924234,
		"date_joined" : datetime.date.today(),
		"profession" : "developer"
		}



		self.bad_data = {
		"date_of_birth" : "Edith",
		"email": "8341232",
		"phone_number" : "me"


		}

	def test_teacher_form_accepts_valid_data(self):
		form = TeacherForm(self.data)
		self.assertTrue(form.is_valid())


	def test_teacher_form_rejects_invalid_data(self):
		form = TeacherForm(self.bad_data)
		self.assertFalse(form.is_valid())	
		