from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Student 

# Define a resource class
class StudentResource(resources.ModelResource):
    class Meta:
        model = Student

# Register with the resource class
@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource
    