from rest_framework import serializers
from .forms import StudentForm
from .models import Student

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id'] + list(StudentForm.Meta.fields)