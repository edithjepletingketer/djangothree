from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","registeration_number","email","date_joined","profile_picture")
    search_fields=("registeration_number","email","last_name")
    
        
admin.site.register(Teacher,TeacherAdmin)
# Register your models here.
