from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display=("name","duration_in_months","course_number","description")
    search_fields=("course_number","teacher__last_name","description")
    list_filter=("teacher__last_name",)
        
admin.site.register(Course,CourseAdmin)
# Register your models here.
