from django.test import TestCase
from student.models import Students
from course.models import Course
from teacher.models import Teacher
import datetime
class StudentCourseTestCase(TestCase):
    def setUp(self):
        self.student_a=Students.objects.create(
            first_name='Jepleting',
            last_name='Alexis',
            date_of_birth=datetime.date(2000,8,13),
            registration_number='662387876',
            place_of_residence='ghggfg',
            email="edithjepleting@gmail.com",
            phone_number='07345442323',
            guardian_no='09878654',
            id_no='001',
            date_joined=datetime.date.today(),
            
    
            )
        self.student_b=Students.objects.create(
            first_name='lucy',
            last_name='kamoyu',
            date_of_birth=datetime.date(2000,8,13),
            registration_number='6623890',
            place_of_residence='ghggfg',
            email="edithjepleting@gmail.com",
            phone_number='089076744',
            guardian_no='0980084',
            id_no='002',
            date_joined=datetime.date.today(),
            
    
            )
        self.course_b=Course.objects.create(
            name="python",
           duration_in_months="4",
           course_number="667765",
           description="data",
            )
        self.teacher_c=Teacher.objects.create(
            first_name="lucy",
            last_name="Njeri",
            registration_number="6677865",
            place_of_residence="Nairobi",
            phone_number="076533323",
            email="edithjepleting@gmail.com",
            id_no="987768787",
            date_joined=datetime.date.today(),
            date_of_birth=datetime.date(2000,8,13),
            profession="Developer"
    )
        self.python =Course.objects.create(
            name="python",
           duration_in_months="5",
           description="the use solving data to provide solution",
            )
        self.javascript =Course.objects.create(
            name="Javascript",
           duration_in_months="6",
           description="creating fast and impressive website to people",
            )
        self.hardware =Course.objects.create(
            name="hardware",
           duration_in_months="4",
           description="creating and designing different",
            )
        self.teacher =Teacher.objects.create(
            first_name="jenny",
            last_name="chepkopus",
            registration_number="66005",
            place_of_residence="Nairobi",
            phone_number="07777999",
            email="edithjepleting20@gmail.com",
            id_no="987768787",
            date_joined=datetime.date.today(),
            date_of_birth=datetime.date(2000,8,13),
            profession="Designer"
            )
    def test_student_can_join_many_courses(self):
        self.assertEqual(self.student_a.courses.count(),0)
        self.student_a.courses.add(self.python)
        self.assertEqual(self.student_a.courses.count(),1)
        self.student_a.courses.add(self.javascript)
        self.assertEqual(self.student_a.courses.count(),2)
        self.student_a.courses.add(self.hardware)
        self.assertEqual(self.student_a.courses.count(),3)
    def test_course_can_have_many_students(self):
        self.python.student.add(self.student_a,self.student_b)
        self.assertEqual(self.python.student.count(),2)
    def test_teacher_can_have_many_courses(self):
        self.javascript.teacher = self.teacher
        self.hardware.teacher = self.teacher
        self.assertEqual(self.javascript.teacher,self.hardware.teacher)
    
        
    def test_course_can_only_have_one_teacher(self):
        self.python.teacher = self.teacher_a
        self.assertEqual(self.python.teacher.first_name, "Edith")
        self.python.teacher = self.teacher_b
        self.assertEqual(self.python.teacher.first_name, "Jepleting")
    
    def test_course(self):
        self.python.teacher = self.teacher.b
        self.student.courses.add(self.python)
        teachers = self.student.teachers()
        self.assertTrue(self.teacher_b in teachers)    

