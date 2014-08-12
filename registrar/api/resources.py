from tastypie.fields import ToManyField
from tastypie.resources import ModelResource
from registrar.models import Student, Class

__author__ = 'Michael'

class StudentResource(ModelResource):
    class Meta:
        queryset = Student.objects.all()
        resource_name = "student"

        
class ClassResource(ModelResource):
    students = ToManyField(StudentResource, 'students', full=True)

    class Meta:
        queryset = Class.objects.all()
        resource_name = "class"