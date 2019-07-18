from django.contrib import admin
from .models import Students

class StudentAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","registeration_number","email","date_joined","profile_picture")
    search_fields=("registeration_number","email","last_name")
    list_filter=("date_joined","date_of_birth")
        
admin.site.register(Students,StudentAdmin)


# Register your models here.
