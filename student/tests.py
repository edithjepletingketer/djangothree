from django.test import TestCase
from .models import Students
import datetime
from .forms import StudentForm
from django.urls import reverse
from django.test import Client

client = Client() 

# Create your tests here.
# class StudentTestCase(TestCase):
#     def setUp(self):
#         self.student=Students(
#             first_name="Edith",
#             last_name="Jepleting",
#             email="edithjepleting@gmail.com",
#             id_no=33703368,
#             phone_number="071722635",
#             registration_number="0987658",
#             guardian_no="0717222635",
#             date_of_birth=datetime.date.today(),
            
#             )

#     def test_full_name_contains_first_name(self):
#         self.assertIn(self.student.first_name, self.student.full_name())

#     def test_full_name_contains_last_name(self):
#         self.assertIn(self.student.last_name, self.student.full_name()) 
    
#     def test_age_above_18(self):
#         self.assertFalse(self.student.clean() < 18)
#     def test_age_below_30(self):
#         self.assertFalse( self.student.clean() > 30)



class CreateStudentTestCase(TestCase):
    def setUp(self):
        self.data={
        "first_name": "Edith",
        "last_name": "Jepleting",
        "date_of_birth": datetime.date.today(),
        "email": "edithjepleting@gmail.com",
        "id_no": 33703368,
        "phone_number": "071722635",
        "registration_number": "0987658",
        "guardian_no": "0728322635",
        "date_joined" : datetime.date.today()

        }

        self.bad_data={
        "first_name": " ",
        "last_name": "Jepleting",
        "date_of_birth": "datetime.date.today()",
        "email": 1243546542,
        "id_no": "33703368",
        "phone_number": " ",
        "registration_number": "0987658",
        "guardian_no": " "
        }

    def test_student_form_always_valid_data(self):
        form=StudentForm(self.data)
        self.assertFalse(form.is_valid())
    
    def test_student_form_reject_invalid_data(self):
        form=StudentForm(self.bad_data)
        self.assertFalse(form.is_valid())   

    def test_add_student_view(self):
        url = reverse("add_student")
        request = client.post(url, self.data)
        self.assertEqual(request.status_code, 400)


    def test_add_student_views(self):
        url = reverse("add_student")
        request = client.post(url, self.bad_data)
        self.assertEqual(request.status_code, 400)
    